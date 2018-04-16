# -*- coding: UTF-8 -*-
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from security.processadores import user_proc, grupo_proc


def _login(request):
    template = 'admin/login.html'
    _username = request.POST.get('_username', None)
    _password = request.POST.get('_password', None)
    _next = request.GET.get('next', None)
    if request.method == 'POST':
        user = authenticate(username=_username, password=_password)
        if user:
            if user.is_active:
                login(request, user)
                # Outras implemtações para acesso ao sistema aqui.
                if _next:
                    return redirect(_next)
                else:
                    return redirect('manager:index')
            else:
                messages.warning(request, 'Conta de usuário esta bloqueado para acessar o sistema.', 'alert-warning')
        else:
            messages.warning(request, 'Usuário ou senha invalida! Corrija e tente novamente.', 'alert-warning')

    return render(request, template)

@login_required(login_url='/security/login/')
def _logout(request):
    messages.success(request, 'Sessão encerrada com sucesso.', 'alert-success')
    logout(request)
    try:
        pass
        #encerrar todas as sessões carregadas
        #del request.session['permissao']
    except KeyError:
        pass
    _next = request.GET.get('next', None)
    if _next:
        return redirect(_next)
    else:
        return redirect('security:login')


def create_update_user(request, user_id=None):
    if user_id:
        action = request.GET.get('action', None)
        if not action:
            action = 'update'
        return user_proc.view(request, action=action, user_id=user_id)
    else:
        return user_proc.view(request, action='create')


def list_user(request):
    return user_proc.view(request, action='list')


def create_update_grupo(request, grupo_id=None):
    action = request.GET.get('action', None)
    if grupo_id:
        if not action:
            action = 'update'
        return grupo_proc.view(request, action=action, grupo_id=grupo_id)
    else:
        return grupo_proc.view(request, action='create')


def list_grupo(request):
    return grupo_proc.view(request, action='list')