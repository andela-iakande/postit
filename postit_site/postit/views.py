from django.db.models import Q
from rest_framework import generics

from .models import Post
from .permissions import IsOwnerOrReadOnly

from .serializers import ( 
    PostListSerializer, 
    PostDetailSerializer, 
    PostCreateUpdateSerializer
    )   

from rest_framework.permissions import (
    AllowAny, 
    IsAuthenticated,
    IsAdminUser,
    IsAuthenticatedOrReadOnly,
    )
from .pagination import LimitOffsetPagination, PostPageNumberPagination

class PostCreateAPIView(generics.CreateAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = Post.objects.all()
    serializer_class = PostCreateUpdateSerializer
    permission_classes = [IsAuthenticated]
   
    def perform_create(self, serializer):
        """Save the post data when creating a new Post."""
        serializer.save(user=self.request.user)

class PostDetailAPIView(generics.RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostDetailSerializer
    lookup_field = 'slug'

class PostDeleteAPIView(generics.DestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostDetailSerializer
    lookup_field = 'slug'   
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly ] 

class PostListAPIView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostListSerializer
    pagination_class = PostPageNumberPagination

    def get_queryset(self, *args, **kwargs):
        queryset_list = Post.objects.all()
        query = self.request.GET.get("q")
        if query: 
            queryset_list = queryset_list.filter(
                Q(title__icontains=query)|
                Q(content__icontains=query)|
                Q(user__first_name__icontains=query)|
                Q(user__last_name__icontains=query)
                ).distinct()
        return queryset_list    

        
class PostUpdateAPIView(generics.RetrieveUpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostDetailSerializer
    lookup_field = 'slug' 
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def perform_update(self, serializer):
        """Save the post data when creating a new Post."""
        serializer.save(user=self.request.user)    


        
    