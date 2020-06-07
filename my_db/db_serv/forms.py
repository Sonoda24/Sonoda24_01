# -*- coding: utf-8 -*-
"""
Created on Sat May 30 10:14:03 2020

@author: user
"""
from django import forms

class UploadFileForm(forms.Form):
    title = forms.CharField(max_length=50)
    file = forms.FileField()
    
