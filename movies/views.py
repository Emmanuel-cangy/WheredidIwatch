from django.shortcuts import render
from django.http import HttpResponse
from .models import Question, Choice
# Create your views here.
def index(request):
    latest_movie_list = Question.objects.all()
    output = ', '.join([q.movie_name for q in latest_movie_list])
    return HttpResponse(output)
