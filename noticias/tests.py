from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from core.models import Organizacao, Perfil
from .models import Post, Comentario

class DashboardTest(TestCase):
    def setUp(self):
        org_a = Organizacao.objects.create(nome="Org A")
        org_b = Organizacao.objects.create(nome="Org B")

        self.user_a = User.objects.create_user(username="ana", password="123")
        perfil_a = Perfil.objects.create(
            usuario=self.user_a, organizacao=org_a, papel="admin")

        self.user_b = User.objects.create_user(
            username="bruno", password="123")
        perfil_b = Perfil.objects.create(
            usuario=self.user_b, organizacao=org_b, papel="operador")

        p1 = Post.objects.create(organizacao=org_a, autor=perfil_a,
                                 titulo="Post A1", conteudo="Texto", estados="Publicado")
        Post.objects.create(organizacao=org_a, autor=perfil_a,
                            titulo="Post A2", conteudo="Texto")
        Comentario.objects.create(post=p1, autor_nome="Leitor", texto="Bom!")

        Post.objects.create(organizacao=org_b, autor=perfil_b,
                            titulo="Post B1", conteudo="Texto")

    def test_isolamento_metricas_por_organizacao(self):
        self.client.force_login(self.user_a)
        resp = self.client.get(reverse("dashboard"))
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.context["kpis"]["total_posts"], 2)
        self.assertEqual(resp.context["kpis"]["total_comentarios"], 1)

    def test_operador_nao_exporta_csv(self):
        self.client.force_login(self.user_b)
        resp = self.client.get(reverse("exportar_csv"))
        self.assertEqual(resp.status_code, 403)
