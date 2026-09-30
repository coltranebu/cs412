# mini_insta/urls.py
# Coltrane Margosian. coltrane@bu.edu. 2026-09-29
# This file defines which URLs point to which views.

from django.urls import path
from .views import ProfileListView, ProfileDetailView

urlpatterns = [
    path('', ProfileListView.as_view(), name="show_all_profiles"),
    path('profile/<int:pk>', ProfileDetailView.as_view(), name="show_profile"),
]
