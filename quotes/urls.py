# urls.py
# Coltrane Margosian. coltrane@bu.edu. 2026-09-08
# This file assigns URLs to views, linking what is visible in the address bar
# to the backend of the website.

from django.urls import path
from django.conf import settings
from . import views

# URL patterns specific to the quotes app:
urlpatterns = [
    path(r'', views.quote, name="quote"),
    path(r'quote', views.quote, name="quote"),
    path(r'show_all', views.show_all, name="show_all"),
    path(r'about', views.about, name="about"),
]