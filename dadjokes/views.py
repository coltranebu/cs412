from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from rest_framework import generics
from .models import Joke, Picture
from .serializers import *

import random

# Define lists containing PK of every Joke and Picture
joke_pk_list = list(Joke.objects.all().values_list('pk', flat=True))
picture_pk_list = list(Picture.objects.all().values_list('pk', flat=True))

# Create your views here.
class RandomJokeView(TemplateView):
    """Define a view which displays a random joke and picture."""
    template_name = "dadjokes/random_joke.html"

    def get_context_data(self, **kwargs):
        """Return the random Joke and Picture context data."""
        # Get context
        context = super().get_context_data()
        # Add random Joke to context
        rand_joke_pk = joke_pk_list[random.randint(0,len(joke_pk_list)-1)]
        context['joke'] = Joke.objects.get(pk=rand_joke_pk)
        # Add random Picture to context
        rand_pic_pk = picture_pk_list[random.randint(0,len(picture_pk_list)-1)]
        context['picture'] = Picture.objects.get(pk=rand_pic_pk)
        return context

class AllJokesView(ListView):
    """Define a view which displays a list of every Joke."""
    template_name = "dadjokes/all_jokes.html"
    model = Joke
    context_object_name = "jokes"

class AllPicturesView(ListView):
    """Define a view which displays a list of every Picture."""
    template_name = "dadjokes/all_pictures.html"
    model = Picture
    context_object_name = "pictures"

class JokeView(DetailView):
    """Define a view which displays one Joke given its primary key."""
    template_name = "dadjokes/joke.html"
    model = Joke
    context_object_name = "joke"

class PictureView(DetailView):
    """Define a view which displays one Picture given its primary key."""
    template_name = "dadjokes/picture.html"
    model = Picture
    context_object_name = "picture"

class AllJokesAPIView(generics.ListCreateAPIView):
    """Define an API view which lists or creates Jokes."""
    queryset = Joke.objects.all()
    serializer_class = JokeSerializer

class JokeAPIView(generics.RetrieveAPIView):
    """Define an API view which retrieves, updates, and/or destorys a Joke."""
    queryset = Joke.objects.all()
    serializer_class = JokeSerializer

class AllPicturesAPIView(generics.ListAPIView):
    """Define an API view which lists or creates Picture."""
    queryset = Picture.objects.all()
    serializer_class = PictureSerializer

class PictureAPIView(generics.RetrieveAPIView):
    """Define an API view which gets, updates, and/or destorys a Picture."""
    queryset = Picture.objects.all()
    serializer_class = PictureSerializer

class RandomJokeAPIView(generics.ListAPIView):
    """Define an API view which RUD a random Joke."""
    def get_queryset(self):
        """Limits output to just one random Joke."""
        rand_joke_pk = joke_pk_list[random.randint(0,len(joke_pk_list)-1)]
        return Joke.objects.all().filter(pk=rand_joke_pk)
    serializer_class = JokeSerializer

class RandomPictureAPIView(generics.ListAPIView):
    """Define an API view which RUD a random Picture."""
    def get_queryset(self):
        """Limits output to just one random Picture."""
        rand_pic_pk = picture_pk_list[random.randint(0,len(picture_pk_list)-1)]
        return Picture.objects.all().filter(pk=rand_pic_pk)
    serializer_class = PictureSerializer
