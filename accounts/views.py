from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.core.validators import validate_email
from django.contrib.auth.models import User
from django.contrib import messages

from accounts.forms import CadastroForm


def login(request):
    if request.method == 'POST':
        usuario = request.POST['usuario']
        senha = request.POST['senha']
        user = auth.authenticate(request, username=usuario, password=senha)
        if user is not None:
            auth.login(request, user)
            return redirect('listagem')
        else:
            return redirect('login')
    else:
        return render(request, 'accounts/login.html')


def logout(request):
    auth.logout(request)
    return redirect('login')


def cadastro(request):
    context = {}
    form = CadastroForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        new_user = User.objects.create_user(
            username=user.username,
            email=user.email,
            password=user.password,
            first_name=user.first_name,
            last_name=user.last_name,
            is_active=True,
            is_staff=False,
            is_superuser=True)
        new_user.save()
        return redirect('login')

    context['form'] = form
    return render(request, "accounts/cadastro.html", context)
