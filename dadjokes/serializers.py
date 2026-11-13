# dadjokes/serializers.py
# Coltrane Margosian. coltrane@bu.edu. 2026-11-12
# This file defines all serializers in dadjokes, which convert Django data
# models to a text representation suitable to transmit over HTTP.

from rest_framework import serializers
from .models import *

class JokeSerializer(serializers.ModelSerializer):
    """Define a serializer for the Joke model."""
    class Meta:
        """Define the metadata for JokeSerializer."""
        model = Joke
        fields = ['text', 'name', 'timestamp']
    
    '''
    def create(self, validated_data):
        """Override the superclass method that handles object creation."""
        print(f'JokeSerializer.create, validated_data={validated_data}.')
        # Attach FK for the 
        validated_data[]
    '''

class PictureSerializer(serializers.ModelSerializer):
    """Define a serializer for the Picture model."""
    class Meta:
        """Define the metadata for PictureSerializer."""
        model = Picture
        fields = ['image_url', 'timestamp']