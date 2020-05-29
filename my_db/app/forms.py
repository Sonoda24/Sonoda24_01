# -*- coding: utf-8 -*-
"""
Created on Sun Jul 21 23:37:23 2019

@author: user
"""
from django import forms

class UploadFileForm(forms.Form):
    # formのname 属性が 'file' になる
    file = forms.FileField(required=True, label='')
    