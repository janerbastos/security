# -*- coding: UTF-8 -*-
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect


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
    _logout(request)
    try:
        del request.session['permissao']
    except KeyError:
        pass
    _next = request.GET.get('next', None)
    if _next:
        return redirect(_next)
    else:
        return redirect('manager:index')