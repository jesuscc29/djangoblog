from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.views.generic import ListView


def office_home(request):
    context = dict()
    request_context = RequestContext(request, context)
    return render_to_response('office/office_home.html',
                              request_context)