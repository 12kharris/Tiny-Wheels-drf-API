from django.http import Http404
from django.db.models import Count
from rest_framework import generics, filters
from rest_framework.response import Response
from rest_framework.views import APIView
from django_filters.rest_framework import DjangoFilterBackend
from drf_api.permissions import IsOwnerOrReadOnly
from .models import Collections
from .serializers import CollectionSerializer


class CollecionsList(generics.ListAPIView):
    queryset = Collections.objects.all()#.order_by('-Profile.Created_at')
    serializer_class = CollectionSerializer


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
            collection.Views = collection.Views + 1
            collection.save()

        serializer = CollectionSerializer(collection, context={"request": request})
        return Response(serializer.data)