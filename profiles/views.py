from django.db.models import Count
from django.db.models.functions import Length
from rest_framework import generics, filters
from django_filters.rest_framework import DjangoFilterBackend
from drf_api.permissions import IsOwnerOrReadOnly
from .models import Profile
from .serializers import ProfileSerializer


class ProfileList(generics.ListAPIView):
    queryset = Profile.objects.all().order_by("User")
    serializer_class = ProfileSerializer
    filter_backends = [
        filters.OrderingFilter,
        filters.SearchFilter,
    ]
    search_fields = [
        "User__id",
        "User__username",
        "Name"
    ]
    ordering_fields = [
        "User__username",
        "Name",
        "Created_at"
    ]


# generics.RetrieveUpdateDestroyAPIView if want to implement deletion
class ProfileDetail(generics.RetrieveUpdateAPIView):
    """
    Retrieve or update a profile if you're the owner.
    """
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Profile.objects.all().order_by('-Created_at')
    serializer_class = ProfileSerializer
