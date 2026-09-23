# restaurant/urls.py
# Coltrane Margosian. coltrane@bu.edu. 2026-09-17
# This file assigns URLs to views, linking what is visible in the address bar
# to the backend of the website.

from django.urls import path
from django.conf import settings
from . import views

urlpatterns = [
    path(r'', views.main, name='main'),
    path(r'main', views.main, name='main'),
    path(r'order', views.order, name='order'),
    path(r'confirmation', views.confirmation, name='confirmation'),
]
