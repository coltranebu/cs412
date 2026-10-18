# mini_insta/admin.py
# Coltrane Margosian. coltrane@bu.edu. 2026-09-29
# This file adds all models to the admin page.

from django.contrib import admin

# Register your models here.
from .models import Profile, Post, Photo, Follow, Comment, Like
admin.site.register(Profile)
admin.site.register(Post)
admin.site.register(Photo)
admin.site.register(Follow)
admin.site.register(Comment)
admin.site.register(Like)