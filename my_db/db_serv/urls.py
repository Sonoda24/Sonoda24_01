# -*- coding: utf-8 -*-
"""
Created on Sat May 30 10:17:22 2020

@author: user
"""
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('detail/', views.detail, name='detail'),
    path('file_upload/', views.file_upload, name='file_upload'),
]

