from rest_framework import serializers
from .models import Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ["autor", "titulo", "conteudo",
                  "categoria", "estados", "tags"]
