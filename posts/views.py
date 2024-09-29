from django.db.models import Count, Q
from .models import Post, Tag
from profiles.models import Profile
from likes.models import LikeDislike
from .serializers import PostSerializer, TagSerializer
from rest_framework import generics, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from drf_api.permissions import IsOwnerOrReadOnly_Profile


class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.annotate(
        #https://stackoverflow.com/questions/11418522/django-how-to-annotate-queryset-with-count-of-filtered-foreignkey-field
        Likes_count = Count("likedislike", filter=Q(likedislike__IsLike = True)),
        Dislikes_count = Count("likedislike", filter=Q(likedislike__IsLike = False))
    ).order_by("-Created_at")
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


class LikedPostList(generics.ListAPIView):
    serializer_class = PostSerializer

    def get_queryset(self):
        user = self.request.user
        logged_in_profile = Profile.objects.filter(User=user)
        liked_posts = LikeDislike.objects.select_related("likedislike").filter(Profile=logged_in_profile)
        return liked_posts
    

class TagList(generics.ListAPIView):
    queryset = Tag.objects.all().order_by("TagName")
    serializer_class = TagSerializer