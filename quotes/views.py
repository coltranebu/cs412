# views.py
# Coltrane Margosian. coltrane@bu.edu. 2026-09-08
# This file is responsible for the python calculations run before each page is
# loaded. It includes a list of quotes and images which are selected from and
# pushed to the frontend.

from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

# Used to randomly select quotes and images.
import random

# List of Sun Ra quotes.
QUOTE_LIST = ["You're not real, if you were you'd have some status among the nations of the world. So we are both myths.",
    "If death is the absence of life, then death's death is life.",
    "In some far off place, many light years in space, I'll wait for you. Where human feet have never trod, where human eyes have never seen. I'll build a world of abstract dreams and wait for you.",
    "The earth cannot move without music. The earth moves in a certain rhythm, a certain sound, a certain note. When the music stops the earth will stop and everything upon it will die.",
    "If you're not mad at the world, you don't have what it takes.",
    "The first thing to do is to consider time as officially ended. We work on the other side of time."]


def generate_quote():
    """Return a random quote from the list of six."""
    return QUOTE_LIST[random.randint(0,5)]

def generate_img_list():
    """Return a list containing links to each Sun Ra picture."""
    # List which will contain the links to each Sun Ra picture.
    ls = []

    # Adds to list "quotes/sunra/sunra1.jpg", "quotes/sunra/sunra2.jpg", etc.
    i = 1
    while i <= 6:
        ls.append("quotes/sunra/sunra" + str(i) + ".jpg")
        i += 1

    return ls

# --- VIEWS ---

def quote(request):
    """Returns a rendered quote.html using a random quote and image."""
    template_name = 'quotes/quote.html'
    # a dict of context variables (key-value pairs)
    context = {
        "rand_quote": generate_quote(),
        "rand_image": "quotes/sunra/sunra" + str(random.randint(1,6)) + ".jpg"
    }
    return render(request, template_name, context)

def show_all(request):
    """Returns a rendered show_all.html using every quote and image."""
    template_name = 'quotes/show_all.html'
    # a dict of context variables (key-value pairs)
    context = {
        "quote_list": QUOTE_LIST,
        "image_list": generate_img_list(),
    }
    return render(request, template_name, context)

def about(request):
    """Returns a rendered about.html. No context variables."""
    template_name = 'quotes/about.html'
    return render(request, template_name)
