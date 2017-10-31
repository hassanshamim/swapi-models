import json

from django.core import serializers
from django.core.exceptions import ValidationError
from django.http import HttpResponse, JsonResponse, Http404
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt


from .models import Planet
from .serializers import PlanetSerializer

# for People view
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from .models import People
from .serializers import PeopleSerializer

# people class based view
from rest_framework.views import APIView

# species generic views
from rest_framework import generics
from .serializers import SpeciesSerializer
from .models import Species

# Custom pagination
from rest_framework import pagination


@csrf_exempt
def planet_list(request, format=None):
    if request.method == 'GET':
        planets = Planet.objects.all()[:5]

        serializer = PlanetSerializer(planets, many=True)
        return JsonResponse(serializer.data, safe=False)
    else:
        # convert request data from json to a dictionary and create a planet from it
        data = json.loads(request.body)
        serializer = PlanetSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        else:
            return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def planet_detail(request, pk):
    planet = get_object_or_404(Planet, pk=pk)

    if request.method == 'GET':
        serializer = PlanetSerializer(planet)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = json.loads(request.body)
        # update our planet object if those keys are present in the request
        serializer = PlanetSerializer(planet, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        else:
            return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        planet.delete()
        return HttpResponse(status=204)


# Let's make our People Views with DRF api views so we can compare
@api_view(['GET', 'POST']) # Automatically return HTTP 405 if the request type is not set
def people_list(request, format=None):
    if request.method == 'GET':
        people = People.objects.all()
        serializer = PeopleSerializer(people, many=True, context={'request': request})
        return Response(serializer.data)
    else:
        serializer = PeopleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'DELETE', 'PUT'])
def people_detail(request, pk, format=None):
    person = get_object_or_404(People, pk=pk)

    if request.method == 'GET':
        serializer = PeopleSerializer(person)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = PeopleSerializer(person, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        person.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# API view

class PeopleList(APIView):

    def get(self, request, format=None):
        people = People.objects.all()
        serializer = PeopleSerializer(people, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = PeopleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PeopleDetail(APIView):

    def get_object(self, pk):
        try:
            return People.objects.get(pk=pk)
        except People.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        person = self.get_object(pk)
        serializer = PeopleSerializer(person)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        person = self.get_object(pk)
        serializers = PeopleSerializer(person, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        person = self.get_object(pk)
        person.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class LargeResultsPagination(pagination.PageNumberPagination):
    page_size = 50
    max_page_size = 50


class SpeciesList(generics.ListCreateAPIView):

    queryset = Species.objects.all()
    serializer_class = SpeciesSerializer
    pagination_class = LargeResultsPagination


class SpeciesDetail(generics.RetrieveUpdateDestroyAPIView):

    queryset = Species.objects.all()
    serializer_class = SpeciesSerializer

