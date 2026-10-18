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

    def get_followers(self):
        """Return a list of Profiles who follow a Profile."""
        follows = Follow.objects.filter(profile=self)
        profiles = []
        # For each Follow object, add to profiles the following person
        for follow in follows:
            profiles.append(follow.follower_profile)
        return profiles

    def get_num_followers(self):
        """Return the number of followers a Profile has."""
        return len(self.get_followers())

    def get_following(self):
        """Return a list of Profiles whom a Profile follows."""
        follows = Follow.objects.filter(follower_profile=self)
        profiles = []
        # For each Follow object, add to profiles the following person
        for follow in follows:
            profiles.append(follow.profile)
        return profiles

    def get_num_following(self):
        """Return the number Profiles whom a Profile follows."""
        return len(self.get_following())
    
    def get_post_feed(self):
        """Return every Post by each Profile a Profile follows."""
        posts = []
        for profile in self.get_following():
            for post in profile.get_all_posts():
                posts.append(post)
        return posts

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

    def get_all_comments(self):
        """Return every Comment associated with a Post."""
        comments = Comment.objects.filter(post=self)
        return comments
    
    def get_likes(self):
        """Return every Like associated with a Post."""
        likes = Like.objects.filter(post=self)
        return likes

    def get_num_likes(self):
        """Return the number of Likes associated with a Post."""
        return len(self.get_likes())

    def get_num_likes_minus_one(self):
        """Return the number of Likes associated with a Post, minus one."""
        # This CANNOT be good functional style, but I do not know how else to
        # get this information 
        return len(self.get_likes()) - 1

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

class Follow(models.Model):
    """Define a relation that associates two profiles; one following other"""
    # profile: person being followed; follower_profile: person following
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, \
    related_name="profile")
    follower_profile = models.ForeignKey(Profile, on_delete=models.CASCADE, \
    related_name="follower_profile")
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Return a string representation of a Follow."""
        # String too long for 80 character width
        return f'{self.follower_profile.display_name} follows {self.profile.display_name}'

class Comment(models.Model):
    """Define a Comment class associated with a Post and a Profle."""
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    text = models.TextField(blank=True)

    def __str__(self):
        """Return a string representation of a Comment."""
        return f'Comment by {self.profile.display_name} on {self.post.__str__()}'

class Like(models.Model):
    """Define a Like class associated with a Profile and a Post."""
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Return a string representation of a Like."""
        return f'{self.profile.display_name} liked {self.post.__str__()}'
