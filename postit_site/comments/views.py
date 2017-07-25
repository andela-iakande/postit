from django.db.models import Q
from django.shortcuts import render
from rest_framework import generics, permissions
from rest_framework.filters import (
        SearchFilter,
        OrderingFilter,
    )
from rest_framework.mixins import DestroyModelMixin, UpdateModelMixin    
from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,
    IsAdminUser,
    IsAuthenticatedOrReadOnly,
)    
from postit.permissions import IsOwnerOrReadOnly
from postit.pagination import PostLimitOffsetPagination, PostPageNumberPagination

from comments.models import Comment
from django.contrib.auth.models import User


from .serializers import (
    CommentListSerializer,
    CommentDetailSerializer,
    create_comment_serializer,
    )

class CommentCreateAPIView(generics.CreateAPIView):
    queryset = Comment.objects.all()
    permission_classes = [IsAuthenticated]
    
    def get_serializer_class(self):
        model_type = self.request.GET.get("type")
       
        slug = self.request.GET.get("slug")
        parent_id = self.request.GET.get("parent_id", None)
        return create_comment_serializer(
                model_type= model_type, 
                slug=slug,
                parent_id=parent_id,
                user=self.request.user
                ) 


class CommentDetailAPIView(DestroyModelMixin, UpdateModelMixin, generics.RetrieveAPIView):
    queryset = Comment.objects.filter(id__gte=0)
    serializer_class = CommentDetailSerializer
    permission_classes = [IsOwnerOrReadOnly]


    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

class CommentListAPIView(generics.ListAPIView):
    serializer_class = CommentListSerializer
    permission_classes = [IsAuthenticated]
    # filter_backends= [SearchFilter, OrderingFilter]
    # search_fields = ['content', 'user__first_name']

    def get_queryset(self, *args, **kwargs):
        queryset_list = Comment.objects.filter(id__gte=0) 
        query = self.request.GET.get("q")
        if query:
            queryset_list = queryset_list.filter(
                    Q(content__icontains=query)|
                    Q(user__first_name__icontains=query) |
                    Q(user__last_name__icontains=query)
                    ).distinct()
        return queryset_list








