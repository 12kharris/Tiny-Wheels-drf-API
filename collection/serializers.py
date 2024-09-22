from rest_framework import serializers
from .models import Collections

class CollectionSerializer(serializers.ModelSerializer):
    Owner = serializers.ReadOnlyField(source="Profile.User.username")
    is_owner = serializers.SerializerMethodField()

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.Profile.User

    class Meta:
        model = Collections
        fields = [
            'id', 'Owner', 'Views', "is_owner"    
        ]