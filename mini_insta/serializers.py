# mini_insta/serializers.py
# Coltrane Margosian. coltrane@bu.edu. 2026-11-16
# This file defines all serializers in mini_insta, which convert Django data
# models to a text representation suitable to transmit over HTTP.

from rest_framework import serializers
from .models import *

class ProfileSerializer(serializers.ModelSerializer):
    """Define a serializer for the Profile model."""
    class Meta:
        """Define the metadata for ProfileSerializer."""
        model = Profile
        fields = '__all__'

class PostSerializer(serializers.ModelSerializer):
    """Define a serializer for the Post model."""
    photos = serializers.SerializerMethodField()
    likes = serializers.SerializerMethodField()
    comments = serializers.SerializerMethodField()
    profile_display_name = serializers.SerializerMethodField()
    class Meta:
        """Define the metadata for PostSerializer."""
        model = Post
        fields = ['id', 'timestamp', 'caption', 'profile', 'photos', 'likes', 'comments', 'profile_display_name']
    
    def get_photos(self, object):
        """Retrieve all Photos associated with a Post."""
        image_urls = []
        photos = Photo.objects.filter(post=object.pk)
        for photo in photos:
            image_urls.append(photo.get_image_url_http())
        return image_urls

    def get_likes(self, object):
        """Get number of likes of a Post."""
        return object.get_num_likes()
    
    def get_comments(self, object):
        """Get all comments of a Post."""
        print(object.get_all_comments_api())
        return object.get_all_comments_api()

    def get_profile_display_name(self, object):
        """Get the display name of the Post's author."""
        return profile.display_name

class PhotoSerializer(serializers.ModelSerializer):
    """Define a serializer for the Photo model."""
    class Meta:
        """Define the metadata for PhotoSerializer."""
        model = Photo
        fields = '__all__'

class FollowSerializer(serializers.ModelSerializer):
    """Define a serializer for the Follow model."""
    class Meta:
        """Define the metadata for FollowSerializer."""
        model = Follow
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
    """Define a serializer for the Comment model."""
    class Meta:
        """Define the metadata for CommentSerializer."""
        model = Comment
        fields = '__all__'

class LikeSerializer(serializers.ModelSerializer):
    """Define a serializer for the Like model."""
    class Meta:
        """Define the metadata for LikeSerializer."""
        model = Like
        fields = '__all__'
