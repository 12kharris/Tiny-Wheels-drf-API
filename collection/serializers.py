from rest_framework import serializers
from .models import Collections, CollectionItem

class CollectionSerializer(serializers.ModelSerializer):
    Owner = serializers.ReadOnlyField(source="Profile.User.username")
    is_owner = serializers.SerializerMethodField()
    items_count = serializers.ReadOnlyField()

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.Profile.User

    class Meta:
        model = Collections
        fields = [
            'id', 'Owner', 'Views', "is_owner", "items_count"
        ]

class CollectionItemSerializer(serializers.ModelSerializer):
    Owner = serializers.ReadOnlyField(source="Collection.Profile.User.username")
    is_owner = serializers.SerializerMethodField()
    SeriesName = serializers.ReadOnlyField(source="Series.SeriesName")
    BrandName = serializers.ReadOnlyField(source="Series.Brand.BrandName")

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.Collection.Profile.User

    class Meta:
        model = CollectionItem
        fields = [
            "id", "Name", "Series", "SeriesName", "BrandName", "Quantity", "Image", "Owner", "is_owner"
        ]