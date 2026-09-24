from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["autor", "titulo", "conteudo",
                  "categoria", "estados", "tags"]

    def clean_conteudo(self):
        conteudo = self.cleaned_data.get('conteudo', '')

        if len(conteudo) < 50:
            raise forms.ValidationError(
                f"O conteúdo da notícia deve ter no mínimo 50 caracteres. O texto atual tem apenas {len(conteudo)}."
            )

        return conteudo
