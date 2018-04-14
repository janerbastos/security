# -*- coding: utf-8 -*-

from django.conf.urls import url

from security.views import _logout, _login

urlpatterns = [
    url(r'^login/$', _login, name='login'),
    url(r'^logout/$', _logout, name='logout')
    ]