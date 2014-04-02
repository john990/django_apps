from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('fascinate.views',
    # Examples:
    # url(r'^$', 'django_apps.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^(?P<img_id>\d+)/$', 'post'),
    url(r'^ajax/(?P<img_id>\d+)/$', 'ajax_post'),
)
