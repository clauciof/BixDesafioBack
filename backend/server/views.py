from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
import json

def cadastro(request):
    return HttpResponse("Cadastro")

def login(request):
    if request.method == "POST":
        data=json.loads(request.body.decode("utf-8"))
        name = data['name']
        password = data['password']
        
        user = authenticate(username=name, password=password)

        if user:
            return HttpResponse("Logado")
        else:
            return HttpResponse("Email ou senha invalidos")

def usuarios(request):
    return HttpResponse("usuarios")

