from django.conf.urls import url
from . import views



urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^video/new/$', views.post_new, name='post_new'),
    url(r'^cutetag/$', views.cutetag, name='cutetag')
]