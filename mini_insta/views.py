# mini_insta/views.py
# Coltrane Margosian. coltrane@bu.edu. 2026-09-29
# This file defines each view used in the website.

from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView,\
DeleteView
from .models import Profile, Post, Photo
from .forms import CreatePostForm, UpdateProfileForm, UpdatePostForm
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

class DeletePostView(DeleteView):
    """Define a view which allows the user to delete a post."""
    model = Post
    template_name = "mini_insta/delete_post_form.html"

    def get_context_data(self, **kwargs):
        """Return the post specific to a deletion."""
        # Get context dictionary
        context = super().get_context_data()
        # Get primary key of the post
        pk = self.kwargs['pk']
        # Get post corresponding to primary key
        post = Post.objects.get(pk=pk)
        context['post'] = post
        return context

    def get_success_url(self):
        """Redirect user to profile after deletion."""
        # find the PK for this post
        pk = self.kwargs['pk']
        # find the Post object:
        post = Post.objects.get(pk=pk)
        # find the PK of the Profile to which this Post is associated:
        profile = post.profile
        # return the URL to redirect to:
        return reverse('show_profile', kwargs={'pk':profile.pk})

class UpdatePostView(UpdateView):
    """Define a view which allows the user to update a post."""
    model = Post
    form_class = UpdatePostForm
    template_name = "mini_insta/update_post_form.html"

    def get_context_data(self, **kwargs):
        """Return the post specific to an update."""
        # Get context dictionary
        context = super().get_context_data()
        # Get primary key of the post
        pk = self.kwargs['pk']
        # Get post corresponding to primary key
        post = Post.objects.get(pk=pk)
        context['post'] = post
        return context

    def get_success_url(self):
        """Redirect user to post after updating it."""    
        # find the PK for this post
        pk = self.kwargs['pk']
        # find the Post object:
        post = Post.objects.get(pk=pk)
        # return the URL to redirect to:
        return reverse('post', kwargs={'pk':post.pk})

class ShowFollowersDetailView(DetailView):
    """Define a view which displays all of a Profile's followers."""
    model = Profile
    template_name = "mini_insta/show_followers.html"

    def get_context_data(self, **kwargs):
        """Return the Profile specific to the DetailView."""
        # Get context dictionary
        context = super().get_context_data()
        # Get primary key of profile the page corresponds to
        pk = self.kwargs['pk']
        # Get profile corresponding to primary key
        profile = Profile.objects.get(pk=pk)
        # Define and return context
        context['profile'] = profile
        return context

class ShowFollowingDetailView(DetailView):
    """Define a view which displays Profiles whom a Profile follows."""
    model = Profile
    template_name = "mini_insta/show_following.html"

    def get_context_data(self, **kwargs):
        """Return the Profile specific to the DetailView."""
        # Get context dictionary
        context = super().get_context_data()
        # Get primary key of profile the page corresponds to
        pk = self.kwargs['pk']
        # Get profile corresponding to primary key
        profile = Profile.objects.get(pk=pk)
        # Define and return context
        context['profile'] = profile
        return context
