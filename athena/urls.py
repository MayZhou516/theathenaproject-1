from django.conf.urls import url

from . import views

import create_problems

urlpatterns = [
    url(r'^$', views.index, name='index'),
]