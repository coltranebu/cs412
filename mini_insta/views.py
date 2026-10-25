# mini_insta/views.py
# Coltrane Margosian. coltrane@bu.edu. 2026-09-29
# This file defines each view used in the website.

from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView,\
DeleteView, TemplateView
from .models import Profile, Post, Photo, User, Follow, Like
from .forms import *
from django.urls import reverse
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

# Create your views here.

class MyLoginRequiredMixin(LoginRequiredMixin):
    """Implements extra features to LoginRequireMixin such as the ability to
    obtain the Profile of the logged in user."""
    login_url = "{% url 'login' %}"

    def get_logged_in_profile(self):
        """Return the Profile corresponding to the user."""
        return Profile.objects.get(user=self.request.user)

    def get_context_data(self, **kwargs):
        """Return the Profile context data."""
        context = super().get_context_data()
        context['profile'] = self.get_logged_in_profile()
        return context

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

class OwnProfileDetailView(MyLoginRequiredMixin, DetailView):
    """Define a view which displays the details of one's own profile."""
    model = Profile
    template_name = "mini_insta/show_profile.html"
    context_object_name = "profile"

    def get_login_url(self):
        """Redirect user to login page if not logged in."""
        return reverse('login')

    def get_object(self):
        """Return the Profile specific to the DetailView."""
        return super().get_logged_in_profile()

class PostDetailView(DetailView):
    """Define a view which displays the details of any one post."""
    model = Post
    template_name = "mini_insta/show_post.html"
    context_object_name = "post"

class CreatePostView(MyLoginRequiredMixin, CreateView):
    """Define a view which allows the user to create a post."""
    form_class = CreatePostForm
    template_name = "mini_insta/create_post_form.html"

    def get_login_url(self):
        """Redirect user to login page if not logged in."""
        return reverse('login')

    def get_success_url(self):
        """Direct the user to a post once it is created."""
        pk = self.kwargs['pk']
        return reverse('post', kwargs={'pk':self.object.pk})

    def get_object(self):
        """Return the Profile specific to the CreateView."""
        return super().get_logged_in_profile()

    def get_context_data(self, **kwargs):
        """Return the Profile specific to the CreateView in context."""
        # Get context dictionary
        context = super().get_context_data()
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

class UpdateProfileView(MyLoginRequiredMixin, UpdateView):
    """Define a view which allows the user to update a profile."""
    model = Profile
    form_class = UpdateProfileForm
    template_name = "mini_insta/update_profile_form.html"
    
    def get_login_url(self):
        """Redirect user to login page if not logged in."""
        return reverse('login')

    def get_object(self):
        """Return the Profile specific to the UpdateView."""
        return super().get_logged_in_profile()

class DeletePostView(MyLoginRequiredMixin, DeleteView):
    """Define a view which allows the user to delete a post."""
    model = Post
    template_name = "mini_insta/delete_post_form.html"

    def get_login_url(self):
        """Redirect user to login page if not logged in."""
        return reverse('login')

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

class UpdatePostView(MyLoginRequiredMixin, UpdateView):
    """Define a view which allows the user to update a post."""
    model = Post
    form_class = UpdatePostForm
    template_name = "mini_insta/update_post_form.html"

    def get_login_url(self):
        """Redirect user to login page if not logged in."""
        return reverse('login')

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

class ShowFeedView(MyLoginRequiredMixin, DetailView):
    """Define a view which displays every Post by every Profile whom a Profile
    follows."""
    model = Profile
    template_name = "mini_insta/show_feed.html"

    def get_login_url(self):
        """Redirect user to login page if not logged in."""
        return reverse('login')

    def get_object(self):
        """Return the Profile specific to the DetailView."""
        return super().get_logged_in_profile()

    def get_context_data(self, **kwargs):
        """Return the Profile specific to the DetailView in context."""
        # Get context dictionary
        context = super().get_context_data()
        return context

class SearchView(MyLoginRequiredMixin, ListView):
    """Define a view which displays Posts and Profiles relevant to a search
    query."""
    template_name = "mini_insta/search_results.html"

    def get_login_url(self):
        """Redirect user to login page if not logged in."""
        return reverse('login')

    def get_object(self):
        """Return the Profile specific to the ListView."""
        return super().get_logged_in_profile()

    def get_context_data(self, **kwargs):
        """Return the Profile specific to the ListView."""
        # Initialize context (with profile)
        context = super().get_context_data()
        # Add query to context
        query = self.request.GET.get('query')
        context['query'] = query
        # Add posts to context
        posts = self.get_queryset()
        context['posts'] = posts
        # Add Profiles with matching display names and usernames to context
        display_name_profiles = \
        Profile.objects.filter(display_name__contains=query)
        username_profiles = \
        Profile.objects.filter(username__contains=query)
        profiles = (display_name_profiles | username_profiles).distinct()
        context['profiles'] = profiles
        # Return context
        return context

    def dispatch(self, request, *args, **kwargs):
        """Render search form if no query. Otherwise, display results."""
        # If no query, redirect to form with blank query and profile info
        if (not 'query' in self.request.GET):
            return render(request, \
            context=({'query' : '', \
            'profile' : super().get_logged_in_profile()}), \
            template_name="mini_insta/search.html")
        # If query, fall back on ListView
        else:
            return super().dispatch(request, *args, **kwargs)
    
    def get_queryset(self):
        """Return the Posts relevant to a query."""
        query = self.request.GET.get('query')
        return Post.objects.filter(caption__contains=query)

class LogoutConfirmationView(TemplateView):
    """Define a view which displays a confirmation page upon logout."""
    template_name = "mini_insta/logged_out.html"

class UserRegistrationView(CreateView):
    """Define a view which allows a person to register as a user."""
    template_name = "mini_insta/register.html"
    form_class = UserCreationForm
    model = User

    def get_success_url(self):
        """Redirect user to login page after registering."""
        return reverse('login')

class CreateProfileView(LoginRequiredMixin, CreateView):
    """Define a view which allows a user to create a profile."""
    model = Profile
    form_class = CreateProfileForm
    template_name = "mini_insta/create_profile_form.html"

    def get_login_url(self):
        """Redirect user to login page if not logged in."""
        return reverse('login')
    
    def get_success_url(self):
        """Direct the user their profile once it is created."""
        return reverse('show_own_profile')

    def get_object(self):
        """Return the Profile specific to the CreateView."""
        return super().get_logged_in_profile()

    def form_valid(self, form):
        """Associate Profile with User on form submission."""
        user = self.request.user
        # Set form user to the user filling it out
        form.instance.user = user
        response = super().form_valid(form)
        return response

class CreateFollowView(MyLoginRequiredMixin, CreateView):
    """Define a view which allows the user to follow a profile."""
    model = Follow
    form_class = CreateFollowForm
    template_name = "mini_insta/create_follow_form.html"

    def get_login_url(self):
        """Redirect user to login page if not logged in."""
        return reverse('login')
    
    def get_success_url(self):
        """Direct the user the profile they followed."""
        return reverse('show_profile', kwargs={'pk':self.kwargs['pk']})

    def get_context_data(self, **kwargs):
        """Return the Profile context data."""
        # Get super context data
        context = super().get_context_data()
        # Get primary key of URL
        pk = self.kwargs['pk']
        # Retrieve the profile being followed
        other_profile = Profile.objects.get(pk=pk)
        # Return context with profile being followed
        context['other_profile'] = other_profile
        return context
    
    def form_valid(self, form):
        """Associate a Follow with two users."""
        # Get primary key of URL
        pk = self.kwargs['pk']
        other_profile = Profile.objects.get(pk=pk)
        # Set form profile to the profile being followed
        form.instance.profile = other_profile

        # Set form follower_profile to profile of the user
        user = self.request.user
        profile = Profile.objects.get(user=user)
        form.instance.follower_profile = profile

        # Return form
        response = super().form_valid(form)
        return response
    
class DeleteFollowView(MyLoginRequiredMixin, DeleteView):
    """Define a view which allows the user to unfollow a Profile."""
    model = Follow
    form_class = DeleteFollowForm
    template_name = "mini_insta/delete_follow_form.html"
    def get_login_url(self):
        """Redirect user to login page if not logged in."""
        return reverse('login')
        
    def get_success_url(self):
        """Direct the user the profile they unfollowed."""
        return reverse('show_profile', kwargs={'pk':self.kwargs['pk']})

    def get_object(self):
        """Return the Follow specific to the deletion."""
        return Follow.objects.get(profile = \
        Profile.objects.get(pk=self.kwargs['pk']),follower_profile= \
        self.request.user.profile)

    def get_context_data(self, **kwargs):
        """Return the Profile context data."""
        context = super().get_context_data()
        # Get URL primary key
        pk = self.kwargs['pk']
        # Get profile being unfollowed
        other_profile = Profile.objects.get(pk=pk)
        # Return context with profile being unfollowed
        context['other_profile'] = other_profile
        return context
        
    def form_valid(self, form):
        """Identify a Follow based on the surrounding information."""
        # Add profile being unfollowed to form
        pk = self.kwargs['pk']
        other_profile = Profile.objects.get(pk=pk)
        form.instance.profile = other_profile

        # Add user's profile to form
        user = self.request.user
        profile = Profile.objects.get(user=user)
        form.instance.follower_profile = profile

        # Return form
        response = super().form_valid(form)
        return response

class CreateLikeView(MyLoginRequiredMixin, CreateView):
    """Define a view which allows the user to like a post."""
    model = Like
    form_class = CreateLikeForm
    template_name = "mini_insta/create_like_form.html"

    def get_login_url(self):
        """Redirect user to login page if not logged in."""
        return reverse('login')
    
    def get_success_url(self):
        """Direct the user the post they liked."""
        return reverse('post', kwargs={'pk':self.kwargs['pk']})

    def get_context_data(self, **kwargs):
        """Return the Post context data."""
        context = super().get_context_data()
        pk = self.kwargs['pk']
        post = Post.objects.get(pk=pk)
        # Return context data with Post being liked
        context['post'] = post
        return context
    
    def form_valid(self, form):
        """Associate a Like with a Post and a Profile."""
        # Add Post being liked to form
        pk = self.kwargs['pk']
        post = Post.objects.get(pk=pk)
        form.instance.post = post

        # Add user's Profile to form
        user = self.request.user
        profile = Profile.objects.get(user=user)
        form.instance.profile = profile

        # Return form
        response = super().form_valid(form)
        return response

class DeleteLikeView(MyLoginRequiredMixin, DeleteView):
    """Define a view which allows the user to unlike a Post."""
    model = Follow
    form_class = DeleteLikeForm
    template_name = "mini_insta/delete_like_form.html"
    def get_login_url(self):
        """Redirect user to login page if not logged in."""
        return reverse('login')
        
    def get_success_url(self):
        """Direct the user the post they unliked."""
        return reverse('post', kwargs={'pk':self.kwargs['pk']})

    def get_object(self):
        """Return the Like specific to the deletion."""
        return Like.objects.get(post = \
        Post.objects.get(pk=self.kwargs['pk']),profile= \
        self.request.user.profile)

    def get_context_data(self, **kwargs):
        """Return the Post context data."""
        context = super().get_context_data()
        pk = self.kwargs['pk']
        post = Post.objects.get(pk=pk)
        # Add Post being unliked to context
        context['post'] = post
        return context
        
    def form_valid(self, form):
        """Identify a Like based on the surrounding information."""
        # Add post to form
        pk = self.kwargs['pk']
        post = Post.objects.get(pk=pk)
        form.instance.post = post

        # Add user's Profile to form
        user = self.request.user
        profile = Profile.objects.get(user=user)
        form.instance.profile = profile

        # Return form
        response = super().form_valid(form)
        return response
