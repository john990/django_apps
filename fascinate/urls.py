from django.conf.urls import patterns, include, url

from django.contrib import admin
from rest_framework import routers
from fascinate import views

admin.autodiscover()

router = routers.DefaultRouter()
router.register(r'(?P<img_id>\d+)/$', views.api_post)
router.register(r'groups', views.GroupViewSet)

urlpatterns = patterns('fascinate.views',
    # url(r'^$', 'django_apps.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^(?P<img_id>\d+)/$', 'post'),
    url(r'^upload/$', 'upload'),
    # API
    url(r'^api/', include(router.urls)),
    # url(r'^api/(?P<img_id>\d+)/$', 'api_post'),
    # url(r'^api/vote/(?P<img_id>\d+)/$', 'api_post_vote'),
    # url(r'^api/recent/$', 'api_recent'),
    # url(r'^api/popular/$', 'api_popular'),
)
