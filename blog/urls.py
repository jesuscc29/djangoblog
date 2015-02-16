# -*- coding: utf-8 -*-
__author__ = 'jesuscc29'

from django.conf.urls import patterns, url
from .views import *

urlpatterns = patterns('',
                       url(r'^$', BlogHome.as_view(), name='blog_home'),
                       )

