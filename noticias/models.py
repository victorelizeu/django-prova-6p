from django.db import models
from django.contrib.auth.models import User


class Organizacao(models.Model):
    nome = models.CharField(max_length=120)
    data_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.nome


class Perfil(models.Model):
    PAPEIS = [
        ("admin", "Administrador"),
        ("operador", "Operador"),
    ]

    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    organizacao = models.ForeignKey(
        Organizacao, on_delete=models.PROTECT, related_name="perfis"
    )
    papel = models.CharField(max_length=20, choices=PAPEIS, default="operador")
    biografia = models.TextField(blank=True)

    def __str__(self) -> str:
        return f"{self.usuario.username} - {self.organizacao.nome} ({self.papel})"


class Categoria(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.nome


class Tag(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.nome


class Post(models.Model):
    ESTADOS = [
        ("Rascunho", "Rascunho"),
        ("Em_Revisao", "Revisão Editorial"),
        ("Publicado", "Publicado!"),
        ("Rejeitado", "Rejeitado!!"),
    ]

    organizacao = models.ForeignKey(
        Organizacao, on_delete=models.PROTECT, related_name="posts"
    )

    autor = models.ForeignKey(Perfil, on_delete=models.CASCADE, related_name="posts")

    titulo = models.CharField(max_length=150)
    conteudo = models.TextField()
    data = models.DateTimeField(auto_now_add=True)
    estados = models.CharField(max_length=50, choices=ESTADOS, default="Rascunho")

    categoria = models.ForeignKey(
        Categoria, related_name="posts", on_delete=models.SET_NULL, null=True
    )
    tags = models.ManyToManyField(Tag, blank=True, related_name="posts")

    def __str__(self) -> str:
        return self.titulo


class Comentario(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comentarios")
    autor_nome = models.CharField(max_length=100)
    texto = models.TextField()
    aproved = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f"Comentário em {self.post.titulo}"
