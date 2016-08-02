# coding=utf-8
from django.views.generic import ListView
from rest_framework.decorators import api_view
from rest_framework.response import Response

from garnachapi.forms import PlaceForm
from garnachapi.models import PlaceType, Place
from recipes import response_json


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

# ============================= GUI Views ==================================


class PlaceList(ListView):
    template_name = 'gapp/places_list.html'
    context_object_name = 'places'

    def get_queryset(self):
        place_list = Place.objects.all()
        return place_list

    def get_context_data(self, **kwargs):
        context = super(PlaceList, self).get_context_data(**kwargs)
        context['place_form'] = PlaceForm(None)
        return context


def remove_place(request):
    errors = dict()
    if request.method == 'POST':
        place_pk = request.POST.get('place_pk', None)
        if place_pk is not None:
            try:
                place = Place.objects.get(pk=place_pk)
                place.delete()
                return response_json("OK", 200)
            except Place.DoesNotExist:
                errors['error'] = 'El lugar seleccionado no existe.'
                return response_json(errors, 404)
        else:
            errors['error'] = 'Debes seleccionar un lugar a borrar.'
            return response_json(errors, 404)
    else:
        errors['error'] = 'No permitido'
        return response_json(errors, 403)


def create_place(request):
    errors = dict()
    if request.method == 'POST':
        place_form = PlaceForm(request.POST or None)
        place_lat = request.POST.get('lat', None)
        place_lng = request.POST.get('lng', None)
        if place_form.is_valid and place_lat is not None \
                and place_lng is not None:
            new_place = place_form.save(commit=False)
            new_place.latitude = place_lat
            new_place.longitude = place_lng
            new_place.save()
            return response_json("OK", 200)
        else:
            errors['error'] = 'Revise los datos ingresados.'
            return response_json(errors, 500)
    else:
        errors['error'] = 'No permitido'
        return response_json(errors, 403)


def update_place(request, pk):
    errors = dict()
    if request.method == 'POST':
        if pk is not None:
            try:
                place_obj = Place.objects.get(pk=pk)
                place_form = PlaceForm(request.POST, instance=place_obj)
                place_lat = request.POST.get('lat', None)
                place_lng = request.POST.get('lng', None)
                if place_form.is_valid and place_lat is not None \
                        and place_lng is not None:
                    new_place = place_form.save(commit=False)
                    new_place.latitude = place_lat
                    new_place.longitude = place_lng
                    new_place.save()
                    return response_json("OK", 200)
                else:
                    errors['error'] = 'Revise los datos ingresados.'
                    return response_json(errors, 500)
            except Place.DoesNotExist:
                errors['error'] = 'No existe el lugar seleccionado.'
                return response_json(errors, 404)
        else:
            errors['error'] = 'No se indicó un lugar a actualizar.'
            return response_json(errors, 404)
    else:
        errors['error'] = 'No permitido'
        return response_json(errors, 403)


def get_place_details(request):
    errors = dict()
    place_pk = request.GET.get('place_pk', None)
    if place_pk is not None:
        place = Place.objects.filter(pk=place_pk).values(
            'name', 'icon', 'description', 'price', 'palce_type__pk',
            'latitude', 'longitude'
        )
        return response_json(list(place), 200)
    else:
        errors['error'] = 'No se indicó un lugar a actualizar'
        return response_json(errors, 404)

