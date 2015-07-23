from django.conf.urls import patterns, include, url
from django.contrib import admin
from blog.views import BlogHome
from djangoblog import settings

urlpatterns = patterns('',
                       url(r'^$', BlogHome.as_view(), name='home'),
                       url(r'^login/$', 'djangoblog.views.user_login', name='login'),
                       url(r'^logout/$', 'djangoblog.views.user_logout', name='logout'),
                       url(r'^blog/', include('blog.urls'), name='blog_index'),
                       url(r'^consultorio/', include('office.urls'), name='office_home'),
                       url(r'^admin/', include(admin.site.urls)),

                       (r'^static/(?P<path>.*)$', 'django.views.static.serve',
                        {'document_root': settings.STATIC_ROOT}),
                       (r'^media/(?P<path>.*)$', 'django.views.static.serve',
                        {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
                       )
