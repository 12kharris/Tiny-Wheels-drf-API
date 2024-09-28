from django.db import IntegrityError
from rest_framework import serializers
from .models import Follower


class FollowerSerializer(serializers.ModelSerializer):
    FollowingUser = serializers.ReadOnlyField(source="FollowingProfile.User.username")
    FollowedProfileName = serializers.ReadOnlyField(source="FollowedProfile.Name")
    FollowedUser = serializers.ReadOnlyField(source="FollowedProfile.User.username")
    is_owner = serializers.SerializerMethodField()

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.FollowingProfile.User

    def create(self, validated_data):
        try:
            return super().create(validated_data)
        except IntegrityError:
            raise serializers.ValidationError({'detail': 'possible duplicate'})

    class Meta:
        model = Follower
        fields = [
            "id", "FollowingUser",
            "FollowedProfile", "FollowedProfileName", "FollowedUser",
            "is_owner"
        ]