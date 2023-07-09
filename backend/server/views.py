from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login as login_django
from django.contrib.auth.decorators import login_required
import json

def cadastro(request):
    if request.user.is_authenticated:
        u = User.objects.get(username=user.username)
        return JsonResponse({autenticated: True})
    else:
        return JsonResponse({autenticated: False})

def login(request):
    if request.method == "POST":
        data=json.loads(request.body.decode("utf-8"))
        name = data['name']
        password = data['password']
        
        user = authenticate(username=name, password=password)

        if user:
            u = User.objects.get(username=name)
            login_django(request, user)
            if user.is_staff == True:
                return JsonResponse({'user': u.username, 'email': u.email, 'staff': True, 'autenticated': True})
            return JsonResponse({'user': user.username, 'email': user.email, 'staff': False, 'autenticated': True})
        else:
            return JsonResponse({'user': None, 'email': None, 'staff': False,  'autenticated': False})



def usuarios(request):
    if request.user.is_authenticated:
        u = User.objects.get(username=request.user.username)
        return JsonResponse({'autenticated': True})
    else:
        return JsonResponse({'autenticated': False})
