# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from office.views import PatientList, PatientCreate, PatientDetail

__author__ = 'jesuscc29'


urlpatterns = patterns('',
   url(r'^pacientes/$', PatientList.as_view(), name='patient_list'),
   url(r'^pacientes/nuevo/$', PatientCreate.as_view(),
       name='patient_create'),
   url(r'^pacientes/detalle/(?P<pk>\d+)/$', PatientDetail.as_view(),
       name='patient_detail'),
)

