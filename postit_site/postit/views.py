from django.shortcuts import render
from rest_framework import generics, permissions
#from .permissions import IsAuthor
from .serializers import PostDetailSerializer, PostListSerializer
from .models import Post
from django.contrib.auth.models import User

# Create your views here.

# postit/views.py

class PostCreateAPIView(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = Post.objects.all()
    serializer_class = PostDetailSerializer
    #permission_classes = (permissions.IsAuthenticated, IsAuthor)

    def perform_create(self, serializer):
        """Save the post data when creating a new Post."""
        serializer.save()

class PostDeleteAPIView(generics.DestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostDetailSerializer                

class PostDetailAPIView(generics.RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostDetailSerializer

class PostListAPIView(generics.ListAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = Post.objects.all()
    serializer_class = PostDetailSerializer

class PostUpdateAPIView(generics.UpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostListSerializer      



        

     