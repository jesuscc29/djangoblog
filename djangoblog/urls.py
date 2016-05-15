from django.conf.urls import patterns, include, url
from django.contrib import admin
from blog.views import blog_home
from djangoblog import settings
from djangoblog.views import user_login, user_logout
from blog import urls as blog_urls

urlpatterns = patterns('',
                       url(r'^$', blog_home, name='home'),
                       url(r'^login/$', user_login, name='login'),
                       url(r'^logout/$', user_logout, name='logout'),
                       url(r'^blog/', include(blog_urls), name='blog_index'),
                       url(r'^consultorio/', include('office.urls'),
                           name='office_home'),
                       url(r'^admin/', include(admin.site.urls)),

                       (r'^static/(?P<path>.*)$', 'django.views.static.serve',
                        {'document_root': settings.STATIC_ROOT}),
                       (r'^media/(?P<path>.*)$', 'django.views.static.serve',
                        {'document_root': settings.MEDIA_ROOT,
                         'show_indexes': True}),
                       )
