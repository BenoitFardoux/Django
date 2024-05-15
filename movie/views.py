from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse

from movie.models import Movie


def index(request):
    template = loader.get_template("movie/index.html")
    context = {}
    return HttpResponse(template.render(context, request))


def search_movie(request,movie_name):
    status = 200
    context = {}
    if request.method != 'GET':
        status = 405
    else:
        movies = Movie.objects.filter(title__icontains=movie_name)
        context = {'movies':movies}
    return render(request, 'movie/index.html', context, status=status)