# -*- coding: UTF-8 -*-
from django.forms import ModelForm

from manager.models import Grupo


class GrupoForm(ModelForm):

    class Meta:
        model = Grupo
        fields = ['grupo_name',]
        labels = {
            'grupo_name' : 'Nome do grupo',
        }