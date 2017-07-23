from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import (
    # post_create,
    PostCreateAPIView,
    PostDetailAPIView, 
    PostListAPIView,
    PostDeleteAPIView,
    PostUpdateAPIView
)
urlpatterns = {
    url(r'^$', PostListAPIView.as_view(), name='list'),
    # # url(r'^create/$', post_create),
    # url(r'^$', PostListAPIView.as_view(), name = 'list'),
    url(r'^create/$', PostCreateAPIView.as_view(), name="create"),
    url(r'^(?P<slug>[\w-]+)/$', PostDetailAPIView.as_view(), name = 'detail'),
    url(r'^(?P<slug>[\w-]+)/edit/$', PostUpdateAPIView.as_view(), name = 'update'),
    url(r'^(?P<slug>[\w-]+)/delete/$',PostDeleteAPIView.as_view(), name = 'delete'),
}

urlpatterns = format_suffix_patterns(urlpatterns)