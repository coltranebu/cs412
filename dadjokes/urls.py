# dadjokes/urls.py
# Coltrane Margosian. coltrane@bu.edu. 2026-11-12
# This file defines which URLs point to which views.

from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', RandomJokeView.as_view(), name="home"),
    path('random', RandomJokeView.as_view(), name="random_joke"),
    path('jokes', AllJokesView.as_view(), name="all_jokes"),
    path('pictures', AllPicturesView.as_view(), name="all_pictures"),
    path('joke/<int:pk>', JokeView.as_view(), name="joke"),
    path('picture/<int:pk>', PictureView.as_view(), name="picture"),
]
