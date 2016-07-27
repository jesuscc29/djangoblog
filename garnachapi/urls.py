# -*- coding: utf-8 -*-
from django.conf.urls import include, url

from garnachapi.views import place_type, places, places_by_category

__author__ = 'JesusCota'


urlpatterns = (
    url(r'^place_types/', place_type, name='place_type_api'),
    url(r'^places/', places, name='places_api'),
    url(r'^places_by_category/', places_by_category, name='places_by_category'),
    url(r'^api-auth/', include('rest_framework.urls',
                               namespace='rest_framework')),
)
