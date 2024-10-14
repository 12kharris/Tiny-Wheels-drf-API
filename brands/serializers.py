from rest_framework import serializers
from .models import Brand, Series


class BrandSerializer(serializers.ModelSerializer):

    class Meta:
        model = Brand
        fields = [
            'id', 'BrandName'
        ]


class SeriesSerializer(serializers.ModelSerializer):
    BrandName = serializers.ReadOnlyField(source="Brand.BrandName")

    class Meta:
        model = Series
        fields = [
            "id", "SeriesName", "BrandName"
        ]
