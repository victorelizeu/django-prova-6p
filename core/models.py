from django.db import models
from django.contrib.auth.models import User


class Organizacao(models.Model):
    nome = models.CharField(max_length=120)
    data_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome


class DaOrganizacao(models.Model):
    organizacao = models.ForeignKey(
        "core.Organizacao", on_delete=models.PROTECT)

    class Meta:
        abstract = True


class Perfil(models.Model):
    PAPEIS = [
        ("admin", "Administrador"),
        ("operador", "Operador"),
    ]

    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    organizacao = models.ForeignKey(
        'core.Organizacao', on_delete=models.PROTECT, related_name="perfis"
    )
    papel = models.CharField(max_length=20, choices=PAPEIS, default="operador")
    biografia = models.TextField(blank=True)

    def __str__(self) -> str:
        return f"{self.usuario.username} - {self.organizacao.nome} ({self.papel})"
