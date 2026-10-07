# mini_insta/admin.py
# Coltrane Margosian. coltrane@bu.edu. 2026-09-29
# This file adds the Profile, Post, and Photo classes to the admin page.

from django.contrib import admin

# Register your models here.
from .models import Profile, Post, Photo
admin.site.register(Profile)
admin.site.register(Post)
admin.site.register(Photo)
