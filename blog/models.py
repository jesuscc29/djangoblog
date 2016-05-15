# coding=utf-8
import datetime
from django.contrib.auth.models import User
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.text import slugify


@python_2_unicode_compatible
class Post(models.Model):
    title = models.CharField(max_length=155, verbose_name='Título')
    slug = models.SlugField(max_length=155, editable=False)
    author = models.ForeignKey(User, verbose_name='Autor', on_delete=models.PROTECT)
    published_date = models.DateTimeField(default=datetime.datetime.now())
    last_edited = models.DateTimeField(auto_now=True)
    content = models.TextField(verbose_name='Contenido')
    published = models.BooleanField(default=True, verbose_name='Publicar')

    def __str__(self):
        return self.title
