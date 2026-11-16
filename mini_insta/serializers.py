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
    class Meta:
        """Define the metadata for PostSerializer."""
        model = Post
        fields = '__all__'

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
