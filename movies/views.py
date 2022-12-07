from django.shortcuts import render
from django.http import HttpResponse
from .models import Watched, Choice
from django.template import loader
# Create your views here.
def index(request):
    latest_movie_list = Watched.objects.all()
    all_choice_list = Choice.objects.all()
    context = {
        'latest_movie_list': latest_movie_list,
        'all_choice_list': all_choice_list,
    }
    return render(request, 'movies/index.html', context)


def movie(request, watched_id):
    movie = Watched.objects.get(id=watched_id)
    all_choice_list = Choice.objects.all()
    # for provider in providers:
    #     if (movie.provider222() == provider_id):
    #         specificProvider = provider.id

    context = {
        'movie': movie,
        'all_choice_list': all_choice_list,

    }
    return render(request, "movies/movie.html", context)
