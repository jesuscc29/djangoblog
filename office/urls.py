# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from office.views import PatientList, PatientCreate, PatientDetail, save_patient_stats

__author__ = 'jesuscc29'


urlpatterns = patterns('',
   url(r'^pacientes/$', PatientList.as_view(), name='patient_list'),
   url(r'^pacientes/nuevo/$', PatientCreate.as_view(),
       name='patient_create'),
   url(r'^pacientes/detalle/(?P<pk>\d+)/$', PatientDetail.as_view(),
       name='patient_detail'),
   url(r'^save_patient_stats/(?P<pk>\d+)/$', save_patient_stats,
       name='save_patient_stats'),
)

