# -*- coding:UTF-8 -*-
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.template.loader import render_to_string

from security.forms.user_form import UserForm, UserEditForm, UserResetPassword


def create(request, **kwargs):
    template = 'comum/forms.html'
    form = UserForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        user.save()
        return redirect('security:list_user')

    context = {
        'titulo': 'Gestor de Usuários',
        'page_nane': 'Usuários',
        'detail_page_name': 'Você esta cadastrando um novo usuário',
        'form': form,
        'action': 'Usuário',
        'user': None,
        'users': None
    }

    return render(request, template, context)


def update(request, **kwargs):
    template = 'comum/forms.html'
    user = kwargs.get('user', None)
    form = UserEditForm(request.POST or None, instance=user)
    if form.is_valid():
        user = form.save(commit=False)
        user.save()
        return redirect('security:list_user')

    context = {
        'titulo': 'Gestor de Usuários',
        'page_nane': 'Usuários',
        'detail_page_name': 'Você esta atualizando um usuário',
        'form': form,
        'action': 'Usuário',
        'user': None,
        'users': None
    }

    return render(request, template, context)


def resetar_senha(request, user):
    '''
    Metor que responsável por modificar a senha do usuário
    :param request: requisição
    :param user: objeto da classe User
    :return: objeto de reposta no formato json
    '''

    form = UserResetPassword(request.POST or None, instance=user)
    success = False
    if form.is_valid():
        user = form.save(commit=False)
        pwd = request.POST.get('check_password', None)
        user.set_password(pwd)
        user.save()
        success = True

    form_data = render_to_string('security/ajax/forms.html', {'form': form})
    data = {
        'result': form_data,
        'success': success,
    }
    return JsonResponse(data)


def view(request, **kwargs):
    template = 'security/usuarios.html'

    action = kwargs.get('action', None)
    user_id = kwargs.get('user_id', None)
    users = None
    user = None

    if action == 'view':
        user = User.objects.get(username=user_id)

    if action == 'resetar-senha':
        user = User.objects.get(username=user_id)
        return resetar_senha(request, user=user)

    if action == 'create':
        return create(request, **kwargs)

    if action == 'update':
        user = User.objects.get(username=user_id)
        return update(request, user=user)

    if action == 'list':
        users = User.objects.all()

    context = {
        'titulo': 'Gestor de Usuários',
        'page_nane': 'Usuários',
        'detail_page_name': 'Relação de usuários cadastrados',
        'action': 'Usuários',
        'user': user,
        'users': users,
    }

    return render(request, template, context)
