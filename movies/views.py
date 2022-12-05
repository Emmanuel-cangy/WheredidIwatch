from django.shortcuts import render
from django.http import HttpResponse
from .models import Question
# Create your views here.
def index(request):
    latest_question_list = Question.objects.all()
    output = ', '.join([q.movie_name for q in latest_question_list])
    return HttpResponse(output)
