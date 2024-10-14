from django.db import IntegrityError
from rest_framework import serializers
from likes.models import LikeDislike


class LikeDislikeSerializer(serializers.ModelSerializer):
    ProfileName = serializers.ReadOnlyField(source="Profile.Name")
    Username = serializers.ReadOnlyField(source="Profile.User.username")
    LikeType = serializers.SerializerMethodField()

    def get_LikeType(self, obj):
        if obj.IsLike:
            return "like"
        else:
            return "dislike"

    class Meta:
        model = LikeDislike
        fields = [
            "id", "Post", "ProfileName", "Username", "IsLike", "LikeType"
        ]

    def create(self, validated_data):
        try:
            user = self.context['request'].user
            if validated_data["Post"].Profile.User == user:
                raise serializers.ValidationError({
                    'detail': 'cannot like/dislike own post'
                })
            return super().create(validated_data)
        except IntegrityError:
            raise serializers.ValidationError({
                'detail': 'possible duplicate'
            })
