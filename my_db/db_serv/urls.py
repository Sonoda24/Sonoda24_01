# -*- coding: utf-8 -*-
"""
Created on Sat May 30 10:17:22 2020

@author: user
"""
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('list', views.list,name='list'),
    path('new_list', views.new_list, name='new_list'),
    path('get_combo/', views.get_combo, name='get_combo'),
    path('detail/<int:data_id>/', views.detail, name='detail'), 
    path('update/', views.update, name='update'),
    path('file_upload/', views.file_upload, name='file_upload'),
]

