from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.views.generic import ListView, CreateView
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


class PostCreate(CreateView):
    template_name = ''
