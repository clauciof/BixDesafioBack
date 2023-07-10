from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login as login_django
from django.contrib.auth.decorators import login_required
from .models import User as PlatformUser
import pickle
import json


def delete(request):
    if request.method == "POST":
        data = json.loads(request.body.decode("utf-8"))
        print(data)
        user = PlatformUser.objects.get(login=data['login'])
        user.delete()
        return JsonResponse({
            "message":"Excluído com sucesso",
            "status": 200
        }, safe=False)

def update(request):
    if request.method == "POST":
        data = json.loads(request.body.decode("utf-8"))
        print(data)
        user = PlatformUser(
            name = data['name'],
            login = data['login'],
            addres = data['addres'], 
            uf = data['uf'],
            type = data['type'],
            entry = data['entry'],
            out = data['out'],
            holidays = data['holidays']
        )
        user.save(update_fields=['name', 'addres', 'uf', 'type', 'entry', 'out', 'holidays'])
        return JsonResponse({
            "message":"Atualizado com sucesso",
            "status": 200
        }, safe=False)

def usuario(request):
    if request.method == "POST":
        data = json.loads(request.body.decode("utf-8"))
        print(data)
        user = PlatformUser(
            name = data['name'],
            login = data['login'],
            addres = data['addres'], 
            uf = data['uf'],
            type = data['type'],
            entry = data['entry'],
            out = data['out'],
            holidays = data['holidays']
        )
        user.save()
        return JsonResponse({
            "message":"Salvo com sucesso",
            "status": 200
        }, safe=False)

    # try:
    #     if request.method == "GET":
    #         users = list(PlatformUser.objects.values())
    #         return JsonResponse(list(users), safe=False)
    # except Exception as e:
    #         return JsonResponse([], safe=False)
                
    # if request.user.is_authenticated:
    #     u = User.objects.get(username=user.username)
    #     return JsonResponse({authenticated: True})
    # else:
    #     return JsonResponse({authenticated: False})

def login(request):
    try:
        if request.method == "POST":
            data = json.loads(request.body.decode("utf-8"))
            name = data['name']
            password = data['password']
            
            user = authenticate(username=name, password=password)

            if user:
                u = User.objects.get(username=name)
                login_django(request, user)
                if user.is_staff == True:
                    return JsonResponse({'user': u.username, 'email': u.email, 'staff': True, 'authenticated': True})
                return JsonResponse({'user': user.username, 'email': user.email, 'staff': False, 'authenticated': True})
            else:
                return JsonResponse({'user': None, 'email': None, 'staff': False,  'authenticated': False})
    except Exception as e:
        return JsonResponse({'user': None, 'email': None, 'staff': False,  'authenticated': False})



def auth(request):
    try:
        print(request.user)
        if request.method == "GET":
            if request.user.is_authenticated:
                u = User.objects.get(username=request.user.username)
                if request.user.is_staff == True:
                        return JsonResponse({'user': u.username, 'email': u.email, 'staff': True, 'authenticated': True})
                return JsonResponse({'user': u.username, 'email': u.email, 'staff': False, 'authenticated': True})
            else:
                return JsonResponse({'user': None, 'email': None, 'staff': None, 'authenticated': False})
    except Exception as e:
            return JsonResponse({'user': None, 'email': None, 'staff': None, 'authenticated': False})

def usuarios(request):
    try:
        if request.method == "GET":
            users = list(PlatformUser.objects.values())
            return JsonResponse(list(users), safe=False)
    except Exception as e:
            return JsonResponse([], safe=False)
       
