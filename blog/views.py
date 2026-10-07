from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import Article
from .forms import CreateArticleForm, CreateCommentForm
from django.urls import reverse
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

class CreateArticleView(CreateView):
    form_class = CreateArticleForm
    template_name = "blog/create_article_form.html"

class CreateCommentView(CreateView):
    form_class = CreateCommentForm
    template_name = "blog/create_comment_form.html"

    def get_success_url(self):
        pk = self.kwargs['pk']
        return reverse('article', kwargs={'pk':pk})

    def get_context_data(self):
        context = super().get_context_data()
        
        pk = self.kwargs['pk']
        article = Article.objects.get(pk=pk)

        context['article'] = article
        return context

    def form_valid(self, form):
        print(form.cleaned_data)
        # retrieve the PK from the URL pattern
        pk = self.kwargs['pk']
        article = Article.objects.get(pk=pk)
        # attach this article to the comment
        form.instance.article = article

        # delegate the wor kto the superclass method form_valid
        return super().form_valid(form)