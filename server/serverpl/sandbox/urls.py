# -*- coding: utf-8 -*-
#
#  urls.py
#  
#  Copyright 2017 Dominique Revuz <dr@univ-mlv.fr>


from django.conf.urls import url
from sandbox import views


urlpatterns = [
    url(r'^$', views.action),
]
