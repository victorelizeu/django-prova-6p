from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Categoria(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.nome


class Tag(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.nome


class Autor(models.Model):
    nome = models.OneToOneField(User, on_delete=models.CASCADE)
    biografia = models.TextField(blank=True)

    def __str__(self) -> str:
        return self.nome.username


class Post(models.Model):
    ESTADOS = [
        ("Rascunho", "Rascunho"),
        ("Em_Revisao", "Revisão Editorial"),
        ("Publicado", "Publicado!"),
        ("Rejeitado", "Rejeitado!!"),
    ]

    titulo = models.CharField(max_length=150)
    conteudo = models.TextField()
    data = models.DateTimeField(auto_now_add=True)
    estados = models.CharField(max_length=50, choices=ESTADOS, default="Rascunho")

    autor = models.ForeignKey(Autor, on_delete=models.CASCADE, related_name="posts")
    categoria = models.ForeignKey(
        Categoria, related_name="posts", on_delete=models.SET_NULL, null=True
    )
    tags = models.ManyToManyField(Tag, blank=True, related_name="posts")

    def __str__(self) -> str:
        return self.titulo


class Comentario(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="posts")
    autor_nome = models.CharField(max_length=100)
    texto = models.TextField()
    aproved = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.post.titulo}"
