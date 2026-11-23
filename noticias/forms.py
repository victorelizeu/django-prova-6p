from django import forms
from .models import Post, Categoria, Tag
from core.models import Perfil


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["autor", "titulo", "conteudo",
                  "categoria", "estados", "tags"]

    def __init__(self, *args, org=None, **kwargs):
        super().__init__(*args, **kwargs)
        if org:
            self.fields['categoria'].queryset = Categoria.objects.filter(
                organizacao=org)
            self.fields['tags'].queryset = Tag.objects.filter(organizacao=org)
            self.fields['autor'].queryset = Perfil.objects.filter(
                organizacao=org)

    def clean_conteudo(self):
        conteudo = self.cleaned_data.get("conteudo", "")
        if len(conteudo) < 50:
            raise forms.ValidationError(
                f"O conteúdo da notícia deve ter no mínimo 50 caracteres. O texto atual tem apenas {len(conteudo)}."
            )
        return conteudo


class PeriodoForm(forms.Form):
    inicio = forms.DateField(
        required=False,
        widget=forms.DateInput(attrs={"type": "date"})
    )
    fim = forms.DateField(
        required=False,
        widget=forms.DateInput(attrs={"type": "date"})
    )


def filtrar_periodo(request, qs):
    form = PeriodoForm(request.GET)
    if form.is_valid():
        if form.cleaned_data["inicio"]:
            qs = qs.filter(data__date__gte=form.cleaned_data["inicio"])
        if form.cleaned_data["fim"]:
            qs = qs.filter(data__date__lte=form.cleaned_data["fim"])
    return qs, form