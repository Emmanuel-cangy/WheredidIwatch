from django.forms import ModelForm
from .models import Watched
from django import forms
from .models import Choice

class ChoiceForm(ModelForm):
    provider = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter a movie provider"}))
    class Meta:
        model = Choice
        fields = '__all__'

class WatchedForm(ModelForm):
    movie_name = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter a movie name"}))
    movie_description = forms.CharField(widget=forms.Textarea(attrs={"rows": 3}))
    class Meta:
        model = Watched


        # movie_name = form.TextInput()



        fields = ['movie_name', 'movie_description', 'provider222']


        # fields = '__all__'
