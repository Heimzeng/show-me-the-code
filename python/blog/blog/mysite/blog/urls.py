#blog/urls.py

from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^post/(?P<pk>\d+)/$', views.detail, name='detail'),
    url(r'^about/$', views.about, name='about'),
    url(r'^upload/$', views.upload, name='about'),
]