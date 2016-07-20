# coding=utf-8
from django.db import models


class PlaceType(models.Model):
    type = models.CharField(max_length=75, verbose_name='Tipo')
    description = models.TextField(verbose_name='Descripción', blank=True,
                                   null=True)

    def __str__(self):
        return self.type


class Place(models.Model):
    name = models.CharField(max_length=125, verbose_name='Nombre')
    icon = models.CharField(max_length=50, verbose_name='Icono', blank=True,
                            null=True)
    description = models.TextField(verbose_name='Descripción', blank=True,
                                   null=True)
    price = models.CharField(max_length=100, verbose_name='Rango de Peecios',
                             blank=True, null=True)
    latitude = models.CharField(max_length=32, verbose_name='Latitud')
    longitude = models.CharField(max_length=32, verbose_name='Longitud')
    palce_type = models.ForeignKey(PlaceType, verbose_name='Tipo')

    def __str__(self):
        return self.name

