import json

from django.core import serializers
from django.core.exceptions import ValidationError
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt

from .models import Planet


@csrf_exempt
def planet_list(request):
    if request.method == 'GET':
        planets = Planet.objects.all()[:5]
        planets_dicts = [
            {
                'name': planet.name,
                'population': planet.population,
                # Etc...
            }
            for planet in planets]
        planets_json = json.dumps(planets_dicts)
        return HttpResponse(planets_json, content_type='application/json')
    else:
        # convert request data from json to a dictionary and create a planet from it
        data = json.loads(request.body)
        planet = Planet(**data)
        try:
            # validate planet data
            planet.full_clean()
        except ValidationError as e:
            errors = json.dumps(e.message_dict)
            # Return validation errors as json response
            return HttpResponse(errors, content_type='application/json', status=400)
        # Save the planet and return the response as json
        planet.save()
        planet_json = json.dumps(
            {'name': planet.name, 'population': planet.population, 'id': planet.id})
        return HttpResponse(planet_json, content_type='application/json', status=201)


@csrf_exempt
def planet_detail(request, id):
    planet = get_object_or_404(Planet, pk=id)

    if request.method == 'GET':
        desired_keys = ['id', 'name', 'population']
        planet_data = {key: getattr(planet, key) for key in desired_keys}
        planet_json = json.dumps(planet_data)
        return HttpResponse(planet_json, content_type='application/json')

    elif request.method == 'PUT':
        data = json.loads(request.body)
        # update our planet object if those keys are present in the request
        planet.name = data.get('name', planet.name)
        planet.population = data.get('population', planet.population)
        try:
            # validate planet data
            planet.full_clean()
        except ValidationError as e:
            errors = json.dumps(e.message_dict)
            # Return validation errors as json response
            return HttpResponse(errors, content_type='application/json', status=400)
        planet.save()
        desired_keys = ['id', 'name', 'population']
        planet_data = {key: getattr(planet, key) for key in desired_keys}
        planet_json = json.dumps(planet_data)
        return HttpResponse(planet_json, content_type='application/json')

    elif request.method == 'DELETE':
        planet.delete()
        return HttpResponse(status=204)
