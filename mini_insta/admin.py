# mini_insta/admin.py
# Coltrane Margosian. coltrane@bu.edu. 2026-09-29
# This file adds the Profile class to the admin page.

from django.contrib import admin

# Register your models here.
from .models import Profile
admin.site.register(Profile)
