from rest_framework import serializers
from .models import Profile
from followers.models import Follower

class ProfileSerializer(serializers.ModelSerializer):
    OwnerUsername = serializers.ReadOnlyField(source="User.username")
    is_owner = serializers.SerializerMethodField()
    is_followed = serializers.SerializerMethodField()

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.User

    def get_is_followed(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            logged_in_profile = Profile.objects.filter(User=user).first()
            followed = Follower.objects.filter(FollowingProfile=logged_in_profile).filter(FollowedProfile=obj)
            return True if followed.count()==1 else False

    class Meta:
        model = Profile
        fields = [
            'id', 'User', 'OwnerUsername', 'Created_at', 'ProfileImage', 'Name', "is_owner", "is_followed"
        ]