from django.shortcuts import render, render_to_response
from django.template import RequestContext


def blog_home(request):
    var = {}
    var_tmp = RequestContext(request, var)
    return render_to_response('blog/index.html', var_tmp)