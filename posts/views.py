from django.db.models import Count
from .models import Post, Tag
from profiles.models import Profile
from .serializers import PostSerializer, TagSerializer
from rest_framework import generics, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from drf_api.permissions import IsOwnerOrReadOnly_Profile


class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all().order_by("-Created_at")
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [
        filters.SearchFilter,
        DjangoFilterBackend,
    ]
    filterset_fields = [
        'Profile__FollowedProfile__FollowingProfile', #posts from profiles the specified user follows
    ]

    def perform_create(self, serializer):
        logged_in_profile = Profile.objects.filter(User=self.request.user).first()
        serializer.save(Profile = logged_in_profile)


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsOwnerOrReadOnly_Profile]
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    

class TagList(generics.ListAPIView):
    queryset = Tag.objects.all().order_by("TagName")
    serializer_class = TagSerializer