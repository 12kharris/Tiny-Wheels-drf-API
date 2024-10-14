from .models import Comment
from profiles.models import Profile
from .serializers import CommentSerializer
from rest_framework import generics, permissions, filters
from drf_api.permissions import IsOwnerOrReadOnly_Profile
from django_filters.rest_framework import DjangoFilterBackend


class CommentsList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['Post']

    def perform_create(self, serializer):
        logged_in_profile = Profile.objects.filter(User=self.request.user).first()
        serializer.save(Profile=logged_in_profile)


class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsOwnerOrReadOnly_Profile]
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
