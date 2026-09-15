from django.contrib import admin
from .models import Categoria, Comentario, Autor, Tag, Post

# Register your models here.

admin.site.register(Categoria)
admin.site.register(Comentario)
admin.site.register(Autor)
admin.site.register(Tag)
admin.site.register(Post)