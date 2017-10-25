# api/urls.py
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'hello/$', views.hello),
    url(r'hello/(?P<name>[A-Za-z]+)/$', views.hello),
    url(r'planet/$', views.a_planet),
    url(r'film/([0-9]+)/likes/$', views.film_likes),
    url(r'film/([0-9]+)/like/$', views.like_film),
]