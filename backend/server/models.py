from django.db import models

class Usuario(models.Model):
    nome = models.CharField(max_length=100)
    login = models.CharField(max_length=100)
    endereco = models.CharField(max_length=100)
    unidadeFederativa = models.CharField(max_length=2)
    tipo = models.CharField(max_length=10)

