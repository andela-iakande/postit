from django.db.models import Q
from django.shortcuts import render
from rest_framework import generics, permissions
#from .permissions import IsAuthor
from .serializers import (
    PostDetailSerializer,
    PostCreateUpdateSerializer,
    PostListSerializer
)
from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,
    IsAdminUser,
    IsAuthenticatedOrReadOnly,
)

from .permissions import IsOwnerOrReadOnly

from .models import Post
from django.contrib.auth.models import User

# Create your views here.

# postit/views.py

class PostCreateAPIView(generics.CreateAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = Post.objects.all()
    serializer_class = PostCreateUpdateSerializer
    permission_classes = [IsAuthenticated]
    #permission_classes = (permissions.Is Authenticated,  IsAuthor)

    def perform_create(self, serializer):
        """Save the post data when creating a new Post."""
        serializer.save(user=self.request.user )

class PostDeleteAPIView(generics.DestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostDetailSerializer                

class PostDetailAPIView(generics.RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostDetailSerializer

class PostListAPIView(generics.ListAPIView):
    """This class defines the create behavior of our rest api."""
    serializer_class = PostListSerializer

    def get_queryset(self, *args, **kwargs):
        queryset_list = Post.objects.all()
        query = self.request.GET.get("q")
        if query:
            queryset_list = queryset_list.filter(
                Q(title__icontains=query)|
                Q(text__icontains=query)
            ).distinct()
        return queryset_list    



class PostUpdateAPIView(generics.RetrieveUpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostCreateUpdateSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]      

    def perform_update(self, serializer):
        """Save the post data when creating a new Post."""
        serializer.save(user=self.request.user )


        

     