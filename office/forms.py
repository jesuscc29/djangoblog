# -*- coding: utf-8 -*-
from django import forms
from django.forms import ModelForm
from office.models import Patient

__author__ = 'jesuscc29'


class AddPatientForm(ModelForm):
    birthday = forms.DateField(widget=forms.DateInput(format='%Y-%m-%d'),
                               input_formats=('%Y-%m-%d',),
                               label='Fecha de Nacimiento')

    class Meta:
        model = Patient
        fields = ['name', 'last_name', 'gender', 'birthday',
                  'phone_number', 'email']