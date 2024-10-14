from .models import Follower
from profiles.models import Profile
from .serializers import FollowerSerializer
from rest_framework import generics, permissions, filters
from drf_api.permissions import IsOwnerOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend
from drf_api.permissions import IsOwnerOrReadOnly_FollowingProfile


class FollowerList(generics.ListCreateAPIView):
    queryset = Follower.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = FollowerSerializer
    filter_backends = [
        DjangoFilterBackend,
    ]
    filterset_fields = [
        "FollowingProfile__User",
        "FollowedProfile__id"
    ]

    def perform_create(self, serializer):
        logged_in_profile = Profile.objects.filter(User=self.request.user).first()
        serializer.save(FollowingProfile=logged_in_profile)


class FollowerDetail(generics.RetrieveDestroyAPIView):
    queryset = Follower.objects.all()
    permission_classes = [IsOwnerOrReadOnly_FollowingProfile]
    serializer_class = FollowerSerializer
