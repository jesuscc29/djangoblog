# -*- coding: utf-8 -*-
__author__ = 'jesuscc29'

from django.conf.urls import patterns, url
from .views import *

urlpatterns = patterns('',
                       url(r'^$', blog_home, name='blog_home'),
                       )

