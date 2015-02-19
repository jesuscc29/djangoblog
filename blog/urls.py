# -*- coding: utf-8 -*-
__author__ = 'jesuscc29'

from django.conf.urls import patterns, url
from .views import *

urlpatterns = patterns('',
    url(r'^$', BlogHome.as_view(), name='blog_home'),
    url(r'^blog/nuevo/post/$', PostCreate.as_view(), name='new_post'),
)

