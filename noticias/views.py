from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm

# Create your views here.


def lista_posts(request):
    posts = Post.objects.all()
    return render(request, "noticias/lista.html", {"posts": posts})


def novo_post(request):
    if request.method == "POST":
        form = PostForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("lista")
    else:
        form = PostForm()

    return render(request, "noticias/form.html", {"form": form})
