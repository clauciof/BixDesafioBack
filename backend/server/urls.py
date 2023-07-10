from django.urls import path
from . import views

urlpatterns = [
    path('auth/', views.auth, name="auth"), 
    path('usuario/', views.usuario, name="usuario"), 
    path('update/', views.update, name="update"), 
    path('delete/', views.delete, name="delete"), 
    path('usuarios/', views.usuarios, name="usuarios"), 
    path('login/', views.login, name="login"), 
]
