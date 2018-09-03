#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2018/9/3 14:33
# @Author  : feng
# @Site    : 
# @File    : forms.py
# @Software: PyCharm

from django import forms
from .models import Topic

class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['text']
        labels = {'text':''}
