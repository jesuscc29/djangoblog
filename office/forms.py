# -*- coding: utf-8 -*-
from django import forms
from django.forms import ModelForm, DateField
from office.models import Patient, PatientStat, PatientVisit

__author__ = 'jesuscc29'


class AddPatientForm(ModelForm):
    birthday = forms.DateField(widget=forms.DateInput(format='%Y-%m-%d'),
                               input_formats=('%Y-%m-%d',),
                               label='Fecha de Nacimiento')

    class Meta:
        model = Patient
        fields = ['name', 'last_name', 'gender', 'birthday',
                  'phone_number', 'email']


class PatientStatsForm(ModelForm):
    class Meta:
        model = PatientStat
        fields = ['height', 'weight', 'activity', 'stats_date']


class PatientVisitForm(ModelForm):
    class Meta:
        model = PatientVisit
        fields = ['date', 'description']