from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import (
    PostCreateAPIView,
    PostListAPIView,
    PostDetailAPIView,
    PostDeleteAPIView,
    PostUpdateAPIView,
)
urlpatterns = {
    url(r'^$', PostListAPIView.as_view(), name='list'),
    url(r'^create/$', PostCreateAPIView.as_view(), name="create"),
    url(r'^(?P<pk>\d+)/$', PostDetailAPIView.as_view(), name = 'detail'),
    url(r'^(?P<pk>\d+)/edit/$', PostUpdateAPIView.as_view(), name = 'update'),
    url(r'^(?P<pk>\d+)/delete/$',PostDeleteAPIView.as_view(), name = 'delete'),
}

urlpatterns = format_suffix_patterns(urlpatterns)