from django.db import migrations


def org_padrao(apps, schema_editor):
    Org = apps.get_model("core", "Organizacao")
    Categoria = apps.get_model("noticias", "Categoria")
    Tag = apps.get_model("noticias", "Tag")
    Post = apps.get_model("noticias", "Post")

    org, _ = Org.objects.get_or_create(nome="Organização Padrão")

    Categoria.objects.filter(organizacao__isnull=True).update(organizacao=org)
    Tag.objects.filter(organizacao__isnull=True).update(organizacao=org)
    Post.objects.filter(organizacao__isnull=True).update(organizacao=org)


class Migration(migrations.Migration):
    dependencies = [
        ("noticias", "0005_alter_post_autor_categoria_organizacao_and_more"),
    ]

    operations = [migrations.RunPython(org_padrao, migrations.RunPython.noop)]
