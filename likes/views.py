from rest_framework import generics, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from drf_api.permissions import IsOwnerOrReadOnly_Profile
from likes.models import LikeDislike
from likes.serializers import LikeDislikeSerializer
from profiles.models import Profile


class LikeDislikeList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = LikeDislike.objects.all()
    serializer_class = LikeDislikeSerializer

    filter_backends = [
        DjangoFilterBackend,
    ]
    filterset_fields = [
        "Post",
        "IsLike"
    ]

    def perform_create(self, serializer):
        logged_in_profile = Profile.objects.filter(User=self.request.user).first()
        serializer.save(Profile = logged_in_profile)


class LikeDislikeDetail(generics.RetrieveDestroyAPIView):
    permission_classes = [IsOwnerOrReadOnly_Profile]
    serializer_class = LikeDislikeSerializer
    queryset = LikeDislike.objects.all()