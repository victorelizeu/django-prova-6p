from django.urls import path
from . import views

urlpatterns = [
    path("", views.lista_posts, name="lista"),
    path("novo/", views.novo_post, name="novo"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("dashboard/exportar/", views.exportar_posts_csv, name="exportar_csv")
]
