# blog/serializers.py
# A serializer converts a model's data into JSON (data structure)
# for sending/receiving over HTPT (as plaintext)

from rest_framework import serializers
from .models import *

class ArticleSerializer(serializers.ModelSerializer):
    """A serializer for the blog.Article model."""
    class Meta:
        # which model does this serializer work for?
        model = Article
        # specify which fields we want to expose
        fields = ['id', 'title', 'author', 'text', 'published', 'image_file']
    
    def create(self, validated_data):
        """Override the create method. Attach a FK User to a newly created
        article."""
        # Long way:
        # print(f"ArticleListAPIView.create, validated_data={validated_data}")
        
        # # use the POST data to create an Article:
        # article = Article(validated_data)
        # # attach a FK of User; just pick first one (FOR NOW)
        # article.user = User.objects.first() # admin user
        # # save the article to the database:
        # article.save()
        # return article
        
        # Short way:
        kwargs['user'] = User.objects.first()
        # now do the create All at once:
        return Article.objects.create(**kwargs)
