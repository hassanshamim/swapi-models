import json

from django.core import serializers
from django.core.exceptions import ValidationError
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt

from .models import Planet
from .serializers import PlanetSerializer


@csrf_exempt
def planet_list(request):
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
def planet_detail(request, id):
    planet = get_object_or_404(Planet, pk=id)

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
