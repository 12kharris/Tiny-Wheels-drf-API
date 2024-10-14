from django.db import IntegrityError
from rest_framework import serializers
from .models import Follower


class FollowerSerializer(serializers.ModelSerializer):
    FollowingProfileID = serializers.ReadOnlyField(
        source="FollowingProfile.id")
    FollowingUser = serializers.ReadOnlyField(
        source="FollowingProfile.User.username")
    FollowingProfileName = serializers.ReadOnlyField(
        source="FollowingProfile.Name")
    FollowingProfileImage = serializers.ReadOnlyField(
        source="FollowingProfile.ProfileImage.url")
    FollowedProfileName = serializers.ReadOnlyField(
        source="FollowedProfile.Name")
    FollowedUser = serializers.ReadOnlyField(
        source="FollowedProfile.User.username")
    FollowedProfileImage = serializers.ReadOnlyField(
        source="FollowedProfile.ProfileImage.url")
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
            "id", "FollowingProfileID", "FollowingUser",
            "FollowingProfileName", "FollowingProfileImage",
            "FollowedProfile", "FollowedProfileName", "FollowedUser",
            "FollowedProfileImage",
            "is_owner"
        ]
