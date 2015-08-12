# -*- coding: utf-8 -*-
import datetime
from django.http.response import HttpResponse
import simplejson

__author__ = 'jesuscc29'


def date_handler(obj):
    return datetime.datetime.strftime(obj, "%d %b %Y") if hasattr(obj,
                                                                  'isoformat') else obj


def response_json(content, status_code):
    """
    django function only
    Takes a dictionary or value, encode them to json and return a HttpResponse
    @param content: almost any object
    @type content: object
    @param status_code: http status code to return
    @type status_code: int
    @return: json response
    @rtype: HttpResponse
    """
    if not hasattr(content, '__iter__'):
        try:
            content = simplejson.loads(content)
        except ValueError:
            content = dict(data=content)
    content = simplejson.dumps(content, use_decimal=True,
                               default=date_handler)
    return HttpResponse(content=content,
                        status=status_code,
                        content_type='application/json')

