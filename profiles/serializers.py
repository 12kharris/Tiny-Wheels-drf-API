from rest_framework import serializers
from .models import Profile

class ProfileSerializer(serializers.ModelSerializer):
    OwnerUsername = serializers.ReadOnlyField(source="User.username")
    is_owner = serializers.SerializerMethodField()

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.User

    class Meta:
        model = Profile
        fields = [
            'id', 'User', 'OwnerUsername', 'Created_at', 'Image', 'Name', "is_owner"    
        ]