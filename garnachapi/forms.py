# -*- coding: utf-8 -*-
from django.forms import ModelForm, Textarea, HiddenInput

from garnachapi.models import Place

__author__ = 'JesusCota'


class PlaceForm(ModelForm):
    class Meta:
        model = Place
        fields = ['name', 'icon', 'description', 'price', 'palce_type']
        widgets = {
            'description': Textarea(
                attrs={'rows': '3', 'style': 'resize: none;'}),
        }
