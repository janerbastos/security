# -*- coding: UTF-8 -*-
from django.shortcuts import render, redirect, get_object_or_404

from security.forms.grupo_forms import GrupoForm
from manager.models import Grupo


def create(request, **kwargs):
    template = 'comum/forms.html'

    form = GrupoForm(request.POST or None)
    if form.is_valid():
        grupo = form.save(commit=False)
        grupo.grupo_name = grupo.grupo_name.upper()
        grupo.save()
        return redirect('security:list_grupo')

    context = {
        'titulo': 'Gestor de Usuários',
        'page_nane': 'Grupos',
        'detail_page_name': 'Você esta cadastrando um novo grupo',
        'form': form,
        'action': 'Grupos',
        'object': None,
        'objects': None
    }

    return render(request, template, context)


def update(request, grupo):
    template = 'comum/forms.html'
    form = GrupoForm(request.POST or None, instance=grupo)
    if form.is_valid():
        grupo = form.save(commit=False)
        grupo.grupo_name = grupo.grupo_name.upper()
        grupo.save()
        return redirect('security:list_grupo')

    context = {
        'titulo': 'Gestor de Usuários',
        'page_nane': 'Grupos',
        'detail_page_name': 'Você esta editando um novo grupo',
        'form': form,
        'action': 'Grupos',
        'object': None,
        'objects': None
    }

    return render(request, template, context)


def view(request, **kwargs):
    template = 'security/grupos.html'

    action = kwargs.get('action', None)
    grupo_id = kwargs.get('grupo_id', None)
    grupos = None
    action = kwargs.get('action', None)
    if action:
        if action == 'create':
            return create(request, **kwargs)
        elif action == 'update':
            grupo = get_object_or_404(Grupo, id=grupo_id)
            return update(request, grupo)
        elif action == 'list':
            grupos = Grupo.objects.all()

    context = {
        'titulo': 'Gestor de Grupos',
        'page_nane': 'Grupos',
        'detail_page_name': 'Relação de grupos cadastrados',
        'action': 'Grupos',
        'object': None,
        'objects': grupos,
    }

    return render(request, template, context)