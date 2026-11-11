from rest_framework import serializers
from .models import Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ["id", "autor", "titulo", "conteudo",
                  "categoria", "estados", "tags"]

    def validate_conteudo(self, value):
        if len(value) < 50:
            raise serializers.ValidationError(
                "O conteúdo deve ter no mínimo 50 caracteres.")
        return value
