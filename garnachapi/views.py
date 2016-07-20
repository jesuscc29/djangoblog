from rest_framework.decorators import api_view
from rest_framework.response import Response

from garnachapi.models import PlaceType


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

