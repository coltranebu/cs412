# mini_insta/models.py
# Coltrane Margosian. coltrane@bu.edu. 2026-09-29
# This file defines the Profile, Post, and Photo classes for the website's
# database.

from django.db import models

# Create your models here.

class Profile(models.Model):
    """Define a profile class containing biographical information
    about a user."""
    username = models.TextField(blank=True)
    display_name = models.TextField(blank=True)
    profile_image_url = models.TextField(blank=True)
    bio_text = models.TextField(blank=True)
    join_date = models.DateField(auto_now=True)

    def __str__(self):
        """Return a string displaying the profile's display name and
        username."""
        return f'{self.display_name} (@{self.username})'

    def get_all_posts(self):
        """"""
        posts = Post.objects.filter(profile=self)
        return posts


class Post(models.Model):
    """"""
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now=True)
    caption = models.TextField(blank=True)

    def __str__(self):
        """"""
        return f'Post by {self.profile.username} at {self.timestamp}'

    def get_all_photos(self):
        photos = Photo.objects.filter(post=self)
        return photos

class Photo(models.Model):
    """"""
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    image_url = models.URLField(blank=True)
    image_file = models.ImageField(blank=True)
    timestamp = models.DateTimeField(auto_now=True)

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

