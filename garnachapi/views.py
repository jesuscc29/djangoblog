# coding=utf-8
from rest_framework.decorators import api_view
from rest_framework.response import Response

from garnachapi.models import PlaceType, Place


@api_view(['GET'])
def place_type(request):
    response = dict()
    try:
        response['status'] = 200
        response['message'] = PlaceType.objects.all().values('pk', 'type',
                                                             'description')
        return Response(response)
    except Exception as e:
        response['status'] = 500
        response['message'] = 'Error: ' + e.message
        return Response(response)


@api_view(['GET'])
def places(request):
    response = dict()
    try:
        response['status'] = 200
        response['message'] = Place.objects.all().values('name', 'icon',
                                                         'description',
                                                         'price', 'latitude',
                                                         'longitude',
                                                         'palce_type__type')
        return Response(response)
    except Exception as e:
        response['status'] = 500
        response['message'] = 'Error: ' + e.message
        return Response(response)


@api_view(['GET'])
def places_by_category(request):
    response = dict()
    print request.GET
    category = request.GET.get('category', None)
    try:
        if category is not None:
            try:
                response['status'] = 200
                response['message'] = Place.objects.filter(
                    palce_type__type__contains=category
                ).values('name', 'icon', 'description', 'price', 'latitude',
                         'longitude', 'palce_type__type')
                return Response(response)
            except Place.DoesNotExist:
                response['status'] = 200
                response['message'] = list()
                return Response(response)
        else:
            response['status'] = 500
            response['message'] = '¡Debes seleccionar una categoría a buscar!'
            return Response(response)
    except Exception as e:
        response['status'] = 500
        response['message'] = 'Error: ' + e.message
        return Response(response)
