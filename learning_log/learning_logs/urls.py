#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2018/8/30 20:10
# @Author  : feng
# @Site    : 
# @File    : urls.py
# @Software: PyCharm

'''定义learning_logs的URL模式'''
from django.conf.urls import url
from . import views

urlpatterns = [
    #主页
    url(r'^$', views.index, name='index'),

    #显示所有的主题
    url(r'^topics/$', views.topics, name='topics'),

    #特定主题的详细页面
    url(r'^topics/(?P<topic_id>\d+)/$', views.topic, name='topic'),
]

#{% url 'learning_logs:topic' topic.id}