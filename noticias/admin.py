from django.contrib import admin
from .models import Categoria, Tag, Post, Comentario


class PostAdmin(admin.ModelAdmin):
    list_display = ("titulo", "organizacao")
    list_filter = ("organizacao", )


admin.site.register(Post, PostAdmin)
admin.site.register(Categoria)
admin.site.register(Tag)
admin.site.register(Comentario)
