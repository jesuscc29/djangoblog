# -*- coding: utf-8 -*-
__author__ = 'jesuscc29'

from django.conf.urls import patterns, url
from .views import *

urlpatterns = patterns('',
                       url(r'^$', BlogHome.as_view(), name='blog_home'),
                       url(r'^nuevo/post/$', create_post, name='new_post'),
                       url(r'^herramientas/imc/$', imc_calculator,
                           name='imc_calculator'),
                       url(r'^herramientas/peso_ideal/$',
                           ideal_weight_calculator,
                           name='ideal_weight_calculator'),
                       url(r'^post/(?P<pk>\d+)/$', PostSingle.as_view(),
                           name='post_single'),
                       url(r'^gastos_energeticos/$', basal_energy_waste,
                           name='basal_energy_waste'),
                       )

