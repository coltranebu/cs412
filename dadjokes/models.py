# dadjokes/models.py
# Coltrane Margosian. coltrane@bu.edu. 2026-11-12
# This file defines the Joke and Picture models for dadjokes.

from django.db import models

# Create your models here.
class Joke(models.Model):
    """Define the Joke class."""
    text = models.TextField()
    name = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

class Picture(models.Model):
    """Define the Picture class."""
    image_url = models.TextField()
    name = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
