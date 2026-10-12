from django import forms
from .models import Article, Comment

class CreateArticleForm(forms.ModelForm):

    class Meta:
        model = Article
        fields = ['author', 'title', 'text', 'image_file']

class UpdateArticleForm(forms.ModelForm):

    class Meta:
        model = Article
        fields = ['title', 'text']
        

class CreateCommentForm(forms.ModelForm):

    class Meta:

        model = Comment
        fields = ['author', 'text']