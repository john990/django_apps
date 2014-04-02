from django.conf.urls import patterns, include, url

from django.contrib import admin

admin.autodiscover()


urlpatterns = patterns('',
    # url(r'^$', 'django_apps.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^f/', include('fascinate.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
