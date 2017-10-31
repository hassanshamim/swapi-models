from django.conf.urls import url
from . import views

from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    url(r'^planets/$', views.planet_list, name='planet-list'),
    url(r'^planets/(?P<pk>[0-9]+)/$', views.planet_detail, name='planet-detail'),
    url(r'^people/$', views.people_list, name='people-list'),
    url(r'^people/(?P<pk>[0-9]+)/$', views.people_detail, name='people-detail'),
    url(r'^species/$', views.SpeciesList.as_view(), name='species-list'),
    url(r'^species/(?P<pk>[0-9]+)/$', views.SpeciesDetail.as_view(), name='species-detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
