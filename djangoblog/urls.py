from django.conf.urls import patterns, include, url
from django.contrib import admin
from djangoblog import settings

urlpatterns = patterns('',
                       url(r'^$', 'djangoblog.views.home', name='home'),
                       url(r'login/', 'djangoblog.views.login', name='login'),
                       url(r'^blog/', include('blog.urls')),
                       url(r'^admin/', include(admin.site.urls)),

                       (r'^static/(?P<path>.*)$', 'django.views.static.serve',
                        {'document_root': settings.STATIC_ROOT}),
                       (r'^media/(?P<path>.*)$', 'django.views.static.serve',
                        {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
                       )
