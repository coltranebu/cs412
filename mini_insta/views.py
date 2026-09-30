# mini_insta/views.py
# Coltrane Margosian. coltrane@bu.edu. 2026-09-29
# This file defines each view used in the website.

from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Profile

# Create your views here.

class ProfileListView(ListView):
    """Define a view which displays all profiles in a grid."""
    model = Profile
    template_name = "mini_insta/show_all_profiles.html"
    context_object_name = "profiles"

class ProfileDetailView(DetailView):
    """Define a view which displays the details of any one profile."""
    model = Profile
    template_name = "mini_insta/show_profile.html"
    context_object_name = "profile"
