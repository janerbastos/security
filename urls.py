# -*- coding: utf-8 -*-

from django.conf.urls import url

from manager.views import create_update_site, open_site, create_update_user, list_user
from .views import _login

urlpatterns = [
    url(r'^$', _login, name='login'),
    ]