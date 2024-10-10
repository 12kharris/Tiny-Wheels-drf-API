from django.http import Http404
from django.db.models import Count
from rest_framework import generics, filters
from rest_framework.response import Response
from rest_framework.views import APIView
from django_filters.rest_framework import DjangoFilterBackend
from drf_api.permissions import IsOwnerOrReadOnly_CollectionItem
from .models import Collections, CollectionItem
from .serializers import CollectionSerializer, CollectionItemSerializer


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
                print("VIEWS INCREMENTED")
                collection.Views = collection.Views + 1
                collection.save()

            collection_items = CollectionItem.objects.filter(Collection=pk)
            serializer = CollectionItemSerializer(collection_items, context={"request": request}, many=True)
            return Response(serializer.data)
        else: 
            return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)


class CollectionItemDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsOwnerOrReadOnly_CollectionItem]
    serializer_class = CollectionItemSerializer
    queryset = CollectionItem.objects.all()