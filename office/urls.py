# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from office.views import PatientList, PatientCreate, PatientDetail, \
    save_patient_stats, get_patient_stats, \
    edit_patient_stats, remove_patient_status, save_patient_visit, \
    edit_patient_visit, get_patient_visit_details, \
    remove_patient_visit, PersonList, person_add, person_payment_add, \
    get_person_payments, remove_person

__author__ = 'jesuscc29'

urlpatterns = patterns('',
                       url(r'^pacientes/$', PatientList.as_view(),
                           name='patient_list'),
                       url(r'^pacientes/nuevo/$', PatientCreate.as_view(),
                           name='patient_create'),
                       url(r'^pacientes/detalle/(?P<pk>\d+)/$',
                           PatientDetail.as_view(),
                           name='patient_detail'),
                       url(r'^save_patient_stats/(?P<pk>\d+)/$',
                           save_patient_stats,
                           name='save_patient_stats'),
                       url(r'^get_patient_stats/(?P<pk>\d+)/$',
                           get_patient_stats,
                           name='get_patient_stats'),
                       url(r'^edit_patient_stats/(?P<pk>\d+)/$',
                           edit_patient_stats,
                           name='edit_patient_stats'),
                       url(r'^remove_patient_status/(?P<pk>\d+)/$',
                           remove_patient_status,
                           name='remove_patient_status'),
                       url(r'^save_patient_visit/(?P<pk>\d+)/$',
                           save_patient_visit,
                           name='save_patient_visit'),
                       url(r'^edit_patient_visit/(?P<pk>\d+)/$',
                           edit_patient_visit,
                           name='edit_patient_visit'),
                       url(r'^get_patient_visit_details/(?P<pk>\d+)/$',
                           get_patient_visit_details,
                           name='get_patient_visit_details'),
                       url(r'^remove_patient_visit/(?P<pk>\d+)/$',
                           remove_patient_visit,
                           name='remove_patient_visit'),
                       url(r'^personas/$', PersonList.as_view(),
                           name='list_money_count'),
                       url(r'^personas/agregar/$', person_add,
                           name='person_add'),
                       url(r'^personas/pago/nuevo/$', person_payment_add,
                           name='person_payment_add'),
                       url(r'^personas/pago/ver/(?P<pk>\d+)/$',
                           get_person_payments,
                           name='get_person_payments'),
                       url(r'^personas/borrar/(?P<pk>\d+)/$',
                           remove_person,
                           name='remove_person'),
                       )
