from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path("movies/<int:watched_id>/", views.movie, name = "movie"),
    path("movies/addmovie", views.addmovie, name = "addmovie")
]
