# voter_analytics/admin.py
# Coltrane Margosian. coltrane@bu.edu. 2026-11-01
# This file adds all models to the admin page.

from django.contrib import admin

# Register your models here.
from .models import *
admin.site.register(Voter)