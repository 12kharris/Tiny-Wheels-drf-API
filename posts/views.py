from django.db.models import Count
from .models import Post, Tag
from .serializers import PostSerializer, TagSerializer
from rest_framework import generics, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from drf_api.permissions import IsOwnerOrReadOnly


class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all().order_by("-Created_at")
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    

class TagList(generics.ListAPIView):
    queryset = Tag.objects.all().order_by("TagName")
    serializer_class = TagSerializer