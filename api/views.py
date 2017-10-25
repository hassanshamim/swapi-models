from django.http import HttpResponse, Http404 # our response object we must return
from .models import Planet, Film


def hello(request, name='World'):
    text = "Hello %s" % name
    return HttpResponse(text)


def a_planet(request):
    planet_name = Planet.objects.get(pk=1).name
    return HttpResponse(planet_name)


def planet_detail(request, id):
    planet = Planet.objects.get(pk=id)


def film_likes(request, id):
    try:
        film = Film.objects.get(pk=id)
    except Film.DoesNotExist:
        raise Http404

    return HttpResponse("Film %s has %s likes" % (film.title, film.likes))


def like_film(request, id):
    try:
        film = Film.objects.get(pk=id)
    except Film.DoesNotExist:
        raise Http404

    film.like()
    return HttpResponse("Film %s was liked!" % film.title)