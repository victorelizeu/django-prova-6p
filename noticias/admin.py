from django.contrib import admin
from .models import Categoria, Tag, Post, Comentario

admin.site.register(Post)
admin.site.register(Categoria)
admin.site.register(Tag)
admin.site.register(Comentario)
