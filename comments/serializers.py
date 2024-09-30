from django.contrib.humanize.templatetags.humanize import naturaltime
from rest_framework import serializers
from .models import Comment


class CommentSerializer(serializers.ModelSerializer):
    Username = serializers.ReadOnlyField(source='Profile.User.username')
    is_owner = serializers.SerializerMethodField()
    OwnerProfile = serializers.ReadOnlyField(source="Profile.Name")
    OwnerProfileID = serializers.ReadOnlyField(source="Profile.id")
    ProfileImage = serializers.ReadOnlyField(source='Profile.Image.url')
    Created_ago = serializers.SerializerMethodField()

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.Profile.User

    def get_Created_ago(self, obj):
        return naturaltime(obj.Created_at)

    class Meta:
        model = Comment
        fields = [
            "id", "Post", "OwnerProfile", "OwnerProfileID", "Username", "is_owner",
            "ProfileImage", "Created_ago", "Content"
        ]