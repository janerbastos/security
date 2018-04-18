# -*- coding:UTF-8 -*-

from django import template
from django.contrib.auth.models import User
from django.template.loader import render_to_string
from django.utils.html import format_html

from databases.constants import CHOOSE_LISTA_CONTENTS
from mamba.models import Site, ContentType
from manager.models import Grupo, UserSite, Papel

register = template.Library()


@register.assignment_tag()
def has_papel_by_tipo(content_type, **kwargs):
    action = kwargs.get('action', None)
    opcao = kwargs.get('opcao', None)
    if action == 'desvincular-permissao-grupo':
        papeis = kwargs.get('papeis', None)
        if papeis:
            papeis = papeis.filter(content_type__tipo=content_type.tipo)
    else:
        list_papeis = kwargs.get('papeis', 0)
        papeis = Papel.objects.filter(content_type__tipo=content_type.tipo, id__in=list_papeis)

    if not opcao:
        opcao = 'papeis'

    html = render_to_string('security/ajax/forms.html', {'papeis': papeis, 'tipo': content_type.descricao,
                                                         'opcao': opcao})
    return format_html(html)


