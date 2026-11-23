import csv
from .dashboard import calcular_metricas
from .forms import PostForm, filtrar_periodo
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .models import Post, Categoria
from .forms import PostForm
from django.core.exceptions import PermissionDenied
from django.utils import timezone


def org_atual(request):
    if not hasattr(request.user, 'perfil'):
        raise PermissionDenied(
            "Seu usuário não possui um Perfil vinculado a uma Organização.")
    return request.user.perfil.organizacao


@login_required
def lista_posts(request):
    org = org_atual(request)

    filtros = Q()
    q = request.GET.get("q", "").strip()
    categoria_id = request.GET.get("categoria", "").strip()

    if q:
        filtros &= Q(titulo__icontains=q)
    if categoria_id:
        filtros &= Q(categoria_id=categoria_id)

    posts = Post.objects.filter(organizacao=org).filter(filtros)
    categorias = Categoria.objects.filter(organizacao=org)

    conjunto = {
        "posts": posts,
        "categorias": categorias,
    }

    return render(request, "noticias/lista.html", conjunto)


def eh_admin(user):
    return hasattr(user, 'perfil') and getattr(user.perfil, "papel", None) == 'admin'


@login_required
def novo_post(request):
    if not eh_admin(request.user):
        raise PermissionDenied(
            "Apenas administradores podem cadastrar notícias, não operadores.")

    org = org_atual(request)
    form = PostForm(request.POST or None, org=org)
    if form.is_valid():
        post = form.save(commit=False)
        post.organizacao = org
        post.save()
        form.save_m2m()
        return redirect("lista")

    return render(request, "noticias/form.html", {"form": form})


@login_required
def dashboard(request):
    org = org_atual(request)
    base = Post.objects.filter(organizacao=org)
    base, form = filtrar_periodo(request, base)

    contexto = calcular_metricas(base)
    contexto["form"] = form
    contexto["org"] = org
    contexto["eh_admin"] = eh_admin(request.user)

    return render(request, "noticias/dashboard.html", contexto)


@login_required
def exportar_posts_csv(request):
    if not eh_admin(request.user):
        raise PermissionDenied(
            "Apenas administradores podem exportar relatórios.")

    org = org_atual(request)
    qs = Post.objects.filter(organizacao=org).select_related(
        "autor__usuario", "categoria")
    qs, _ = filtrar_periodo(request, qs)

    resp = HttpResponse(content_type="text/csv; charset=utf-8")
    resp["Content-Disposition"] = 'attachment; filename="relatorio_posts.csv"'

    writer = csv.writer(resp)
    writer.writerow(["Título", "Autor", "Categoria", "Estado", "Data"])
    for p in qs:
        writer.writerow([
            p.titulo,
            p.autor.usuario.username,
            p.categoria.nome if p.categoria else "Sem categoria, coloque uma categoria",
            p.get_estados_display(),
            timezone.localtime(p.data).strftime("%d/%m/%Y %H:%M"),
        ])
    return resp
