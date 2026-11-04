from rest_framework import serializers
from .models import Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ["autor", "titulo", "conteudo", "categoria", "estados", "tags"]

        def validate(self, data):

            if len(data) < 50:
                raise serializers.ValidationError(
                    f"O conteúdo da notícia deve ter no mínimo 50 caracteres. O texto atual tem apenas {len(conteudo)}."
                )

            return data
