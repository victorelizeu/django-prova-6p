from django.urls import path
from . import views

urlpatterns = [
    path("", views.lista_posts, name="lista"),
    path("novo/", views.novo_post, name="novo"),
]
