from django.shortcuts import render, redirect
from .models import Post, Categoria
from .forms import PostForm
from django.db.models import Q

# Create your views here.


def lista_posts(request):

    filtros = Q()

    q = request.GET.get("q", "").strip()
    categoria_id = request.GET.get("categoria", "").strip()

    if q:
        filtros &= Q(titulo__icontains=q)

    if categoria_id:
        filtros &= Q(categoria_id=categoria_id)

    posts = Post.objects.filter(filtros)

    categorias = Categoria.objects.all()

    conjunto = {
        "posts": posts,
        "categorias": categorias,
    }

    return render(request, "noticias/lista.html", conjunto)


def novo_post(request):
    if request.method == "POST":
        form = PostForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("lista")
    else:
        form = PostForm()

    return render(request, "noticias/form.html", {"form": form})
