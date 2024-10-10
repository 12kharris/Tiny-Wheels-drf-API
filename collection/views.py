from django.http import Http404, HttpResponseForbidden
from django.db.models import Count
from rest_framework import generics, filters, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from django_filters.rest_framework import DjangoFilterBackend
from drf_api.permissions import IsOwnerOrReadOnly_CollectionItem
from .models import Collections, CollectionItem
from .serializers import CollectionSerializer, CollectionItemSerializer
from profiles.models import Profile


class CollecionsList(generics.ListAPIView):
    queryset = Collections.objects.annotate(
        items_count = Count("collectionitem", distinct=True)
    )
    serializer_class = CollectionSerializer
    filter_backends = [
        DjangoFilterBackend,
    ]
    filterset_fields = [
        "id"
    ]


class CollectionDetail(APIView):
    """
    Get a collections details and update the Views property
    """
    def get_object(self, pk):
        try:
            collection = Collections.objects.get(pk=pk)
            return collection
        except:
            raise Http404

    def get(self, request, pk):
        collection = self.get_object(pk)
        if collection is not None:
            #increment the collection's view count
            if (request.user.username != collection.Profile.User.username):
                collection.Views = collection.Views + 1
                collection.save()

            collection_items = CollectionItem.objects.filter(Collection=pk)
            serializer = CollectionItemSerializer(collection_items, context={"request": request}, many=True)
            return Response(serializer.data)
        else: 
            return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)


class CollectionItemList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = CollectionItemSerializer
    
    def get_queryset(self):
        user = self.request.user
        if user.pk is not None:
            logged_in_profile = Profile.objects.filter(User=user).first()
            collection = Collections.objects.filter(Profile=logged_in_profile).first()
            collection_items = CollectionItem.objects.filter(Collection=collection)
            return collection_items
        else:
            return CollectionItem.objects.none()

class CollectionItemDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsOwnerOrReadOnly_CollectionItem]
    serializer_class = CollectionItemSerializer
    queryset = CollectionItem.objects.all()