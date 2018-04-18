# -*- coding: UTF-8 -*-
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.template.loader import render_to_string
from django.utils.html import format_html

from mamba.models import ContentType
from security.forms.grupo_forms import GrupoForm
from manager.models import Grupo, Papel


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


def permissoes(request, **kwargs):
    grupo = Grupo.objects.get(id=kwargs.get('grupo_id', 0))
    action = kwargs.get('action', None)
    if request.is_ajax():
        if action == 'desvincular-permissao-grupo':
            papeis = grupo.papeis.all()
        else:
            list_papeis = grupo.papeis.all().values_list('id', flat=True)
            papeis = Papel.objects.all().exclude(id__in=list_papeis)
        contents_type = ContentType.objects.all()
        html = render_to_string('security/ajax/forms.html', {'papeis': papeis, 'contents_type': contents_type, 'opcao': 'permissoes', 'action': action})
        data = {
            'Título': 'Lista de Permissões',
            'result': format_html(html)
        }
        return JsonResponse(data)

    template = 'security/permissoes_grupo.html'

    if request.method == 'POST':
        list = request.POST.getlist('papeis')
        for uid in list:
            if action == 'desvincular-permissao-grupo':
                grupo.papeis.remove(uid)
            else:
                papel = Papel.objects.get(id=uid)
                grupo.papeis.add(papel)

        return redirect(request.path+'?action=permissoes')

    context = {
        'titulo': 'Gestor de Permissões',
        'page_nane': 'Permissões',
        'detail_page_name': 'Você esta editando as permissoes do grupo',
        'form': None,
        'action': 'permissões',
        'object': grupo,
        'objects': grupo.papeis.all(),
        'contents_type': ContentType.objects.all(),
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
        elif action in ['vincular-permissao-grupo', 'desvincular-permissao-grupo', 'permissoes']:
            return permissoes(request, **kwargs)
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