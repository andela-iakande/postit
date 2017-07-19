from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Post
from rest_framework.serializers import ModelSerializer

class PostDetailSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = Post
        fields = (
            'id', 
            'title', 
            'text',
            'published_date')
              

class PostCreateUpdateSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = Post
        fields = ( 
            'title', 
            'text',
            'published_date')

class PostListSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = Post
        fields = ( 
            'user',
            'title', 
            'text',
            'published_date')       