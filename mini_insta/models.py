# mini_insta/models.py
# Coltrane Margosian. coltrane@bu.edu. 2026-09-29
# This file defines the Profile class for the website's database.

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
