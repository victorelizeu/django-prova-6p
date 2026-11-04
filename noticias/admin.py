from django.contrib import admin
from .models import Organizacao, Perfil, Categoria, Tag, Post, Comentario


@admin.register(Organizacao)
class OrganizacaoAdmin(admin.ModelAdmin):
    list_display = ("id", "nome")


@admin.register(Perfil)
class PerfilAdmin(admin.ModelAdmin):
    list_display = ("id", "usuario", "organizacao", "papel")


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("id", "titulo", "organizacao", "autor", "estados", "data")
    list_filter = ("organizacao", "estados", "categoria")


admin.site.register(Categoria)
admin.site.register(Tag)
admin.site.register(Comentario)