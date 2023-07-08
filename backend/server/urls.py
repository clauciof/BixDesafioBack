from django.urls import path
from . import views

urlpatterns = [
    path('usuarios/', views.usuarios, name="usuarios"), #get todos os usuarios cadastrados
    path('cadastro/', views.cadastro, name="cadastro"), #post e update de cadastro para novos usuarios
    #path('usuario/email', views.usuario, name="usuairo"), #get e delete
    path('login/', views.login, name="login"), #get e delete
]
