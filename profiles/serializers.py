from rest_framework import serializers
from .models import Profile

class ProfileSerilizer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source="User.username")

    class Meta:
        model = Profile
        fields = [
            'id', 'owner', 'Created_at', 'Image', 'Name'         
        ]