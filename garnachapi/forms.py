# -*- coding: utf-8 -*-
from django.forms import ModelForm, Textarea

from garnachapi.models import Place, PlaceType

__author__ = 'JesusCota'


class PlaceForm(ModelForm):
    class Meta:
        model = Place
        fields = ['name', 'icon', 'description', 'price', 'palce_type']
        widgets = {
            'description': Textarea(
                attrs={'rows': '3', 'style': 'resize: none;'}),
        }


class PlaceTypeForm(ModelForm):
    class Meta:
        model = PlaceType
        fields = ['type', 'description']
        widgets = {
            'description': Textarea(
                attrs={'rows': '3', 'style': 'resize: none;'}),
        }
