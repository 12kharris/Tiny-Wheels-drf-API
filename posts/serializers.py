from rest_framework import serializers
from posts.models import Post, Tag
from profiles.models import Profile
from likes.models import LikeDislike
#from likes.models import Like


class PostSerializer(serializers.ModelSerializer):
    TagName = serializers.ReadOnlyField(source="Tag.TagName")
    TagColour = serializers.ReadOnlyField(source="Tag.Colour")
    OwnerProfile = serializers.ReadOnlyField(source="Profile.Name")
    OwnerProfileID = serializers.ReadOnlyField(source="Profile.id")
    OwnerProfileImage = serializers.ReadOnlyField(source="Profile.ProfileImage.url")
    OwnerUsername = serializers.ReadOnlyField(source="Profile.User.username")
    is_owner = serializers.SerializerMethodField()
    Profile_image = serializers.ReadOnlyField(source='Profile.image.url')
    LikeDislike_id = serializers.SerializerMethodField()
    LikeType = serializers.SerializerMethodField()
    Likes_count = serializers.ReadOnlyField()
    Dislikes_count = serializers.ReadOnlyField()
    Comments_count = serializers.ReadOnlyField()

    def validate_image(self, value):
        if value.size > 2 * 1024 * 1024:
            raise serializers.ValidationError('Image size larger than 2MB!')
        if value.image.height > 4096:
            raise serializers.ValidationError(
                'Image height larger than 4096px!'
            )
        if value.image.width > 4096:
            raise serializers.ValidationError(
                'Image width larger than 4096px!'
            )
        return value

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.Profile.User

    def get_LikeDislike_id(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            logged_in_profile = Profile.objects.filter(User=user).first()
            like_dislike = LikeDislike.objects.filter(
                Profile=logged_in_profile, Post=obj
            ).first()
            return like_dislike.id if like_dislike else None
        return None

    def get_LikeType(self, obj):
        like_id = self.get_LikeDislike_id(obj)
        if like_id is not None:
            liked = LikeDislike.objects.filter(id=like_id).first().IsLike
            return "like" if liked else "dislike"
        return None

    class Meta:
        model = Post
        fields = [
            'id', 'OwnerProfile', "OwnerProfileID", "OwnerProfileImage", "OwnerUsername", 'is_owner', 
            'Profile_image', 'Created_at', 'Updated_at',
            'Title', 'Caption', 'Image', "Tag",
            "TagName", "TagColour",
            "LikeDislike_id", "LikeType", "Likes_count", "Dislikes_count", "Comments_count"
        ]


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = [
            'id', 'TagName', 'Colour'
        ]