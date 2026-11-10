from django.contrib import admin
from .models import Categoria, Tag, Post, Comentario


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("id", "titulo", "organizacao", "autor", "estados", "data")
    list_filter = ("organizacao", "estados", "categoria")


admin.site.register(Categoria)
admin.site.register(Tag)
admin.site.register(Comentario)
