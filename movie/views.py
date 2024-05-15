from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from dotenv import load_dotenv
from movie.models import Movie
import requests

import os

load_dotenv()


def index(request):
    template = loader.get_template("movie/index.html")
    context = {}
    return HttpResponse(template.render(context, request))


def search_movie(request, title):
    status = 200
    context = {}
    if request.method != 'GET':
        status = 405
    else:
        movies = Movie.objects.filter(title__icontains=title)
        # TODO : verifier si la liste est vide
        if len(movies) == 0:
            movies = []
            url = "http://www.omdbapi.com/?s=" + str(title) + "&apikey=" + os.getenv("OMDB_API_KEY")
            response = requests.get(url, request.GET)
            if response.status_code == 200:
                data = response.json()
                for movie in data["Search"]:
                    imdb_id = movie["imdb_id"]
                    request_result = requests.get("http://www.omdbapi.com/?i="
                                                  + imdb_id + "&apikey=" + os.getenv("OMDB_API_KEY")).json()
                    if request_result.status_code == 200:
                        movie_to_add = Movie(title=movie["Title"], year=movie["Year"], poster=movie["Poster"],
                                      genre=request_result['Genre'])
                        movies.append(movie_to_add)
                        movie_to_add.save()
        context = {'movies': movies}

    return render(request, 'movie/index.html', context, status=status)
