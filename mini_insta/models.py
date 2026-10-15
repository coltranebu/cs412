# mini_insta/models.py
# Coltrane Margosian. coltrane@bu.edu. 2026-09-29
# This file defines the Profile, Post, and Photo classes for the website's
# database.

from django.db import models
from django.urls import reverse

# Create your models here.

class Profile(models.Model):
    """Define a profile class containing biographical information
    about a user."""
    username = models.TextField(blank=True)
    display_name = models.TextField(blank=True)
    profile_image_url = models.TextField(blank=True)
    bio_text = models.TextField(blank=True)
    join_date = models.DateField(auto_now_add=True)

    def __str__(self):
        """Return a string displaying a profile's display name and
        username."""
        return f'{self.display_name} (@{self.username})'

    def get_all_posts(self):
        """Return every post associated with a given Profile."""
        posts = Post.objects.filter(profile=self)
        return posts

    def get_absolute_url(self):
        """Return URL corresponding to Profile."""
        return reverse('show_profile', kwargs={'pk':self.pk})


class Post(models.Model):
    """Define a post class associated with a Profile containing a
    timestamp and caption."""
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    caption = models.TextField(blank=True)

    def __str__(self):
        """Return a string displaying a Post's poster and when it was
        posted."""
        return f'Post by {self.profile.username} at {self.timestamp}'

    def get_all_photos(self):
        """Return every Photo associated with a Post."""
        photos = Photo.objects.filter(post=self)
        return photos

class Photo(models.Model):
    """Define a photo class associated with a Post contains a timestamp and
    either a WWW URL to an image or a URL to an uploaded image."""
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    image_url = models.URLField(blank=True)
    image_file = models.ImageField(blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Return a string representation of a Photo."""
        # Conditional accomodates for whether there is a URL or file.
        if self.image_url:
            return f'Photo on post by {self.post.profile.username} saved on \
            {self.timestamp} with URL {self.image_url}'
        else:
            return f'Photo on post by {self.post.profile.username} saved on \
            {self.timestamp} with URL {self.image_file}'
    
    def get_image_url(self):
        """Return the URL to a Photo's image."""
        # If there is a URL, return it. Otherwise, return file.
        if self.image_url:
            return self.image_url
        else:
            return self.image_file.url

