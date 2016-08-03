# -*- coding: utf-8 -*-
from django.conf.urls import include, url

from garnachapi.views import place_type, places, places_by_category, PlaceList, \
    remove_place, create_place, update_place, get_place_details, \
    create_category, remove_category, get_category_details, update_category

__author__ = 'JesusCota'


urlpatterns = (
    url(r'^place_types/', place_type, name='place_type_api'),
    url(r'^places/', places, name='places_api'),
    url(r'^places_by_category/', places_by_category, name='places_by_category'),
    url(r'^api-auth/', include('rest_framework.urls',
                               namespace='rest_framework')),
    # ============= Urls for GUI Managmenet
    url(r'^places_list/$', PlaceList.as_view(), name='place_gui_list'),
    url(r'^remove_place/$', remove_place, name='remove_place'),
    url(r'^create_place/$', create_place, name='create_place'),
    url(r'^update_place/(?P<pk>\d+)/$', update_place, name='update_place'),
    url(r'^get_place_details/$', get_place_details, name='get_place_details'),
    url(r'^create_category/$', create_category, name='create_category'),
    url(r'^remove_category/$', remove_category, name='remove_category'),
    url(r'^get_category_details/$', get_category_details,
        name='get_category_details'),
    url(r'^update_category/(?P<pk>\d+)/$', update_category,
        name='update_category'),
)
