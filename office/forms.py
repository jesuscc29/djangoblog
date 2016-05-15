# -*- coding: utf-8 -*-
from django import forms
from django.forms import ModelForm, DateField
from office.models import Patient, PatientStat, PatientVisit, Person, \
    PersonPayment

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


class PersonForm(ModelForm):
    class Meta:
        model = Person
        fields = ['full_name', 'num_guest', 'total_amount']


class PersonPaymentForm(ModelForm):
    class Meta:
        model = PersonPayment
        fields = ['person', 'payment_date', 'amount_payed']
