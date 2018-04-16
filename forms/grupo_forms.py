# -*- coding: UTF-8 -*-
from django.forms import ModelForm

from manager.models import Grupo


class GrupoForm(ModelForm):

    class Meta:
        model = Grupo
        fields = ['nome',]
        labels = {
            'nome' : 'Nome do grupo',
        }