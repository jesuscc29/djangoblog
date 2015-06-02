# -*- coding: utf-8 -*-
from django.forms import ModelForm
from blog.models import Post

__author__ = 'jesuscc29'


class PostCreateForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'published', 'tags',
                  'featured_image', 'thumbnail']
