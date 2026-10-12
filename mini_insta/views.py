# mini_insta/views.py
# Coltrane Margosian. coltrane@bu.edu. 2026-09-29
# This file defines each view used in the website.

from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .models import Profile, Post, Photo
from .forms import CreatePostForm, UpdateProfileForm
from django.urls import reverse
from django.http import HttpResponse

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

class PostDetailView(DetailView):
    """Define a view which displays the details of any one post."""
    model = Post
    template_name = "mini_insta/show_post.html"
    context_object_name = "post"

class CreatePostView(CreateView):
    """Define a view which allows the user to create a post."""
    form_class = CreatePostForm
    template_name = "mini_insta/create_post_form.html"

    def get_success_url(self):
        """Direct the user to a post once it is created."""
        pk = self.kwargs['pk']
        return reverse('post', kwargs={'pk':self.object.pk})

    def get_context_data(self):
        """Return the profile associated with a post."""
        # Get context dictionary
        context = super().get_context_data()
        # Get primary key of profile the form is for
        pk = self.kwargs['pk']
        # Get profile corresponding to primary key
        profile = Profile.objects.get(pk=pk)
        # Define and return context
        context['profile'] = profile
        return context

    def form_valid(self, form):
        """Create a Post and its associated Photos based on the completed
        form."""
        pk = self.kwargs['pk']
        profile = Profile.objects.get(pk=pk)
        # Attach profile to post
        form.instance.profile = profile
        # Create post
        response = super().form_valid(form)

        # Create new Photo using request.POST object
        # Photo.objects.create(post=self.object, \
        # image_url=self.request.POST['image_url'])

        # Get all images
        files = self.request.FILES.getlist('image_files')
        # Create new Photos based on images
        for file in files:
            Photo.objects.create(post=self.object, image_file=file)
        return response

class UpdateProfileView(UpdateView):
    """Define a view which allows the user to update a profile."""
    model = Profile
    form_class = UpdateProfileForm
    template_name = "mini_insta/update_profile_form.html"
