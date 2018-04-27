# -*- coding: utf-8 -*-

from django.conf.urls import url

from security.views import _logout, _login, list_user, create_update_user, list_grupo, create_update_grupo, _profile

urlpatterns = [
    url(r'^$', _profile, name='profile'),
    url(r'^login/$', _login, name='login'),
    url(r'^logout/$', _logout, name='logout'),
    url(r'^usuarios/$', list_user, name='list_user'),
    url(r'^usuarios/create/$', create_update_user, name='create_user'),
    url(r'^usuarios/(?P<user_id>[\w.@+-]+)/update/$', create_update_user, name='update_user'),
    url(r'^grupos/$', list_grupo, name='list_grupo'),
    url(r'^grupos/create/$', create_update_grupo, name='create_grupo'),
    url(r'^grupos/(?P<grupo_id>\d+)/update/$', create_update_grupo, name='update_grupo'),
    ]