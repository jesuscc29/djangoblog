# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from office.views import office_home

__author__ = 'jesuscc29'


urlpatterns = patterns('',
   url(r'^$', office_home, name='office_home'),
)

