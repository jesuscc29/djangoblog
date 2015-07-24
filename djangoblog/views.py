# -*- coding: utf-8 -*-
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.http.response import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext

__author__ = 'jesuscc29'


# @login_required(login_url='login')
def home(request):
    var = {}
    var_tmp = RequestContext(request, var)
    return render_to_response('index.html', var_tmp)


def user_login(request):
    context = dict()
    errors = dict()
    if request.user.is_authenticated():
        return HttpResponseRedirect(reverse('home'))
    if request.method == 'POST':
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                if 'rememberme' not in request.POST:
                    request.session.set_expiry(900)
                login(request, user)
                request.session['logged'] = True
                request.session['name'] = user.first_name
                url = reverse('home')
                try:
                    url_get = request.META['HTTP_REFERER']
                except KeyError:
                    pass
                else:
                    url_get = url_get.split('next=')
                    if len(url_get) > 1:
                        url = url_get[1]
                return HttpResponseRedirect(url)
            else:
                errors['message'] = 'Tu cuenta ha sido desactivada. ' \
                                    'Contacta a un Administrador.'
        else:
            errors['message'] = 'Tu nombre de usuario o contraseña son ' \
                                'incorrectos.'
    context['errors'] = errors
    request_context = RequestContext(request, context)
    return render_to_response('login.html', request_context)


def user_logout(request):
    logout(request)
    request.session['logged'] = False
    return HttpResponseRedirect(reverse('blog_home'))
