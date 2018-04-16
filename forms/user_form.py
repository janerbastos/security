# -*- coding: UTF-8 -*-
from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.forms.models import ModelForm


class UserForm(ModelForm):
    password = forms.CharField(label='Senha', required=False, widget=forms.PasswordInput())
    check_password = forms.CharField(label='Confirma senha', required=False, widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = (
            'first_name', 'last_name', 'username', 'email', 'is_active', 'password',
        )
        labels = {
            'first_name': 'Primeiro nome',
            'last_name': 'Último nome',
            'username': 'Nome do usuário',
            'email': 'E-Mail',
            'password': 'Senha de acesso',
            'is_active': 'Usuário ativo',
        }

    def clean_check_password(self):
        pws = self.cleaned_data.get('password', None)
        check_pwd = self.cleaned_data.get('check_password', None)

        if pws != check_pwd:
            raise ValidationError('Os dois campos de senha não confirmão')

        return self.cleaned_data.get('pws', None)


class UserEditForm(ModelForm):
    class Meta:
        model = User
        fields = (
            'first_name', 'last_name', 'username', 'email', 'is_active', 'is_staff',
        )
        labels = {
            'first_name': 'Primeiro nome',
            'last_name': 'Último nome',
            'username': 'Nome do usuário',
            'email': 'E-Mail',
            'is_active': 'Usuário ativo',
            'is_staff': 'Site admin',
        }


class UserResetPassword(ModelForm):
    password = forms.CharField(label='Senha', required=True, widget=forms.PasswordInput())
    check_password = forms.CharField(label='Confirma senha', required=False, widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = (
            'password', 'check_password'
        )

    def clean_check_password(self):
        pws = self.cleaned_data.get('password', None)
        check_pwd = self.cleaned_data.get('check_password', None)

        if pws != check_pwd:
            raise ValidationError('Os dois campos de senha não confirmão')

        return self.cleaned_data.get('pws', None)
