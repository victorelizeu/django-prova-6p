from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .models import Post, Categoria
from .forms import PostForm


def org_atual(request):
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


@login_required
def novo_post(request):
    org = org_atual(request)
    form = PostForm(request.POST or None, org=org)

    if form.is_valid():
        post = form.save(commit=False)
        post.organizacao = org
        post.save()
        form.save_m2m()
        return redirect("lista")

    return render(request, "noticias/form.html", {"form": form})
