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
