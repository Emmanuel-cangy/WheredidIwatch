from django.shortcuts import render
from django.http import HttpResponse
from .models import Question, Choice
from django.template import loader
# Create your views here.
def index(request):
    latest_movie_list = Question.objects.all()
    context = {
        'latest_movie_list': latest_movie_list,
    }
    return render(request, 'movies/index.html', context)


def movie(request, question_id=1):
    movie = Question.objects.get(id=question_id)
    context = {
        'movie': movie,
    }
    return render(request, "movies/movie.html", context)
