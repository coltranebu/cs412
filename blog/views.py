from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Article
import random

# Create your views here.
class ShowAllView(ListView):
    model = Article
    template_name = "blog/show_all.html"
    context_object_name = "articles"

class ArticleView(DetailView):
    model = Article
    template_name="blog/article.html"
    context_object_name = "article"

class RandomArticleView(DetailView):
    model = Article
    template_name="blog/article.html"
    context_object_name = "article"
    def get_object(self):
        all_articles = Article.objects.all()
        article = random.choice(all_articles)
        return article