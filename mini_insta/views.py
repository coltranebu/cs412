# mini_insta/views.py
# Coltrane Margosian. coltrane@bu.edu. 2026-09-29
# This file defines each view used in the website.

from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import Profile, Post, Photo
from .forms import CreatePostForm
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
        pk = self.kwargs['pk']
        return reverse('post', kwargs={'pk':self.object.pk})

    def get_context_data(self):
        """"""
        # get context dictionary
        context = super().get_context_data()
        # get primary key of profile the form is for
        pk = self.kwargs['pk']
        # get profile corresponding to primary key
        profile = Profile.objects.get(pk=pk)
        # define and return context
        context['profile'] = profile
        return context

    def form_valid(self, form):
        """"""
        pk = self.kwargs['pk']
        profile = Profile.objects.get(pk=pk)
        # attach profile to post
        form.instance.profile = profile
        
        # create post
        response = super().form_valid(form)

        # create new Photo using request.POST object
        # Photo.objects.create(post=self.object, \
        # image_url=self.request.POST['image_url'])

        # create new Photos
        files = self.request.FILES.getlist('image_files')
        print(files)
        for file in files:
            Photo.objects.create(post=self.object, image_file=file)

        return response
        

