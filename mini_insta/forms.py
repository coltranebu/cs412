# mini_insta/forms.py
# Coltrane Margosian. coltrane@bu.edu. 2026-10-07
# This file defines the forms present in Mini Insta.

from django import forms
from .models import *

class CreatePostForm(forms.ModelForm):
    """Define a class which creates a form to create a Post."""
    class Meta:
        """Define a class containing the meta aspects of CreatePostForm."""
        model = Post
        fields = ['caption']

class UpdateProfileForm(forms.ModelForm):
    """Define a class which creates a form to update a Profile."""
    class Meta:
        """Define a class containing the meta aspects of UpdateProfleForm."""
        model = Profile
        fields = ['display_name', 'profile_image_url', 'bio_text']

class UpdatePostForm(forms.ModelForm):
    """Define a class which creates a form to update a Post."""
    class Meta:
        """Define a class containing the meta aspects of UpdatePostForm."""
        model = Post
        fields = ['caption']

class CreateProfileForm(forms.ModelForm):
    """Define a class which creates a form to create a Profile."""
    class Meta:
        """Define a class containing the meta aspects of CreateProfileForm."""
        model = Profile
        fields = ['username', 'display_name', 'profile_image_url', 'bio_text']

class CreateFollowForm(forms.ModelForm):
    """Define a class which creates a form to create a Follow."""
    class Meta:
        """Define a class containing the meta aspects of CreateFollowForm."""
        model = Follow
        fields = []
    
class DeleteFollowForm(forms.ModelForm):
    """Define a class which creates a form to delete a Follow."""
    class Meta:
        """Define a class containing the meta aspects of DeleteFollowForm."""
        model = Follow
        fields = []

class CreateLikeForm(forms.ModelForm):
    """Define a class which creates a form to create a Like."""
    class Meta:
        """Define a class containing the meta aspects of CreateLikeForm."""
        model = Like
        fields = []
    
class DeleteLikeForm(forms.ModelForm):
    """Define a class which creates a form to delete a Like."""
    class Meta:
        """Define a class containing the meta aspects of DeleteLikeForm."""
        model = Like
        fields = []
