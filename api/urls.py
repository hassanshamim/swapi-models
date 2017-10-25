from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^planets/([0-9]+)/$', views.planet_detail),
    url(r'^planets/$', views.planet_list),
]