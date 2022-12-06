from django.db import models


class Choice(models.Model):
    provider = models.CharField(max_length=50,  default='', blank=True)

    def __str__(self):
        return self.provider

class Question(models.Model):
    movie_name = models.CharField(max_length=200)
    movie_description = models.CharField(max_length=300, default='')
    watched_date = models.DateTimeField('date watched')
    provider222 = models.ForeignKey(Choice, on_delete=models.CASCADE)

    def __str__(self):
        return self.movie_name
