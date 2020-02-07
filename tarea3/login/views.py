from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Seguridad

# Create your views here.
def index(request):
    template = loader.get_template('login/login.html')
    context = {}
    return HttpResponse(template.render(context, request))

def auth(request):
    try:
        email = request.GET['email']
        password = request.GET['password']
        # 1. Hacer las validaciones aqui

        # 2. Buscar en la base de datos al usuario

        # 3. Verificar su clave
    except KeyError:
        # Redisplay the login form.
        context = { 'error_message': "No email/password provided" }
        return render(request, 'login/login.html', context)
    else:
        template = loader.get_template('login/home.html')
        context = {
            'email': email,
        }
        return HttpResponse(template.render(context, request))


def home(request, email):
    template = loader.get_template('login/home.html')
    context = {
        'email': email,
    }
    return HttpResponse(template.render(context, request))


def register(request):
    template = loader.get_template('login/register.html')
    context = {}
    return HttpResponse(template.render(context, request))


def register_user(request):
    try:
        email = request.POST['email']
        password = request.POST['password']
        password_2 = request.POST['password_2']
        # 1. Hacer las validaciones

        # 2. Ingresar los datos en la base

    except KeyError:
        # Redisplay the register form.
        context = { 'error_message': "No email/password provided" }
        return render(request, 'login/register.html', context)

    else:
        template = loader.get_template('login/home.html')
        context = {
            'email': email,
        }
        return HttpResponse(template.render(context, request))