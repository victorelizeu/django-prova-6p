from django.db import models
from core.models import DaOrganizacao, Perfil


class Categoria(DaOrganizacao):
    nome = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.nome


class Tag(DaOrganizacao):
    nome = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.nome


class Post(DaOrganizacao):
    ESTADOS = [
        ("Rascunho", "Rascunho"),
        ("Em_Revisao", "Revisão Editorial"),
        ("Publicado", "Publicado!"),
        ("Rejeitado", "Rejeitado!!"),
    ]

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
