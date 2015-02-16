# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.template import RequestContext

__author__ = 'jesuscc29'


def home(request):
    var = {}
    var_tmp = RequestContext(request, var)
    return render_to_response('index.html', var_tmp)


def login(request):
    var = {}
    var_tmp = RequestContext(request, var)
    return  render_to_response('login.html', var_tmp)
