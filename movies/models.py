from django.db import models

class Question(models.Model):
    movie_name = models.CharField(max_length=200)
    movie_description = models.CharField(max_length=300, default='')
    watched_date = models.DateTimeField('date watched')


    def __str__(self):
        return self.movie_name



# class Choice(models.Model):
#     question = models.ForeignKey(Question, on_delete=models.CASCADE)
#     choice_text = models.CharField(max_length=200)
#     votes = models.IntegerField(default=0)
