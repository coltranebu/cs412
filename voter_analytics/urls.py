# voter_analytics/urls.py
# Coltrane Margosian. coltrane@bu.edu. 2026-11-01
# This file defines which URLs point to which views.

from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views

urlpatterns = [
    path(r'', VotersListView.as_view(), name='home'),
    path(r'results', VotersListView.as_view(), name='voters_list'),
    path(r'voter/<int:pk>', VoterDetailView.as_view(), name='voter_detail'),
    path(r'graphs', GraphListView.as_view(), name='graphs'),
]
