from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^athena/$', views.index, name='index'),
    url(r'^upload/$', views.upload, name='upload'),
]