from rest_framework import generics, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Brand, Series
from .serializers import BrandSerializer, SeriesSerializer


class BrandsList(generics.ListAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
    filter_backends = [
        filters.OrderingFilter,
        filters.SearchFilter,
    ]
    search_fields = [
        "BrandName",
    ]
    ordering_fields = [
        "BrandName"
    ]


class SeriesList(generics.ListAPIView):
    queryset = Series.objects.all()
    serializer_class = SeriesSerializer
    filter_backends = [
        filters.OrderingFilter,
        filters.SearchFilter,
    ]
    search_fields = [
        "BrandName",
        "SeriesName",
    ]
    ordering_fields = [
        "BrandName",
        "SeriesName"
    ]