# dadjokes/admin.py
# Coltrane Margosian. coltrane@bu.edu. 2026-11-12
# This file adds all models to the admin page.

from django.contrib import admin

# Register your models here.

from .models import Joke, Picture
admin.site.register(Joke)
admin.site.register(Picture)
