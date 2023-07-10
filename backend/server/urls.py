from django.urls import path
from . import views

urlpatterns = [
    path('auth/', views.auth, name="auth"), #get todos os usuarios cadastrados
    #path('cadastro/', views.cadastro, name="cadastro"), #post e update de cadastro para novos usuarios
    path('usuario/', views.usuario, name="usuario"), #get e delete
    path('update/', views.update, name="update"), #get e delete
    path('delete/', views.delete, name="delete"), #get e delete
    path('usuarios/', views.usuarios, name="usuarios"), #get e delete
    #path('delete/', views.delete, name="delete"), #get e delete
    path('login/', views.login, name="login"), #get e delete
]
