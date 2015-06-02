# coding=utf-8
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.views.generic import ListView, CreateView
from blog.blog_form import PostCreateForm
from blog.models import *


class BlogHome(ListView):
    template_name = 'blog/index.html'
    paginate_by = 10
    page_kwarg = 'pagina'

    def get_queryset(self):
        return Post.objects.exclude(
            published=False
        )

    def get_context_data(self, **kwargs):
        context = super(BlogHome, self).get_context_data(**kwargs)
        context['last'] = self.request.session.get('last_login', None)

        return context


@login_required(login_url='login')
def create_post(request):
    context = dict()
    form = PostCreateForm(request.POST or None,
                          request.FILES or None)
    if request.method == 'POST':
        post = form.save(commit=False)
        post.author = request.user
        post.save()
        return HttpResponseRedirect(reverse('blog_home'))
    context['form'] = form
    context['operation'] = 'Creación'
    context['subject'] = 'Post'
    request_context = RequestContext(request, context)
    return render_to_response('generic/generic_form.html',
                              request_context)