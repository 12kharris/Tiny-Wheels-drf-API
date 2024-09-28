from rest_framework import serializers
from posts.models import Post, Tag
#from likes.models import Like


class PostSerializer(serializers.ModelSerializer):
    OwnerProfile = serializers.ReadOnlyField(source="Profile.Name")
    OwnerProfileID = serializers.ReadOnlyField(source="Profile.id")
    is_owner = serializers.SerializerMethodField()
    Profile_image = serializers.ReadOnlyField(source='Profile.image.url')
    #like_id = serializers.SerializerMethodField()
    #likes_count = serializers.ReadOnlyField()
    #comments_count = serializers.ReadOnlyField()

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

    def get_like_id(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            like = Like.objects.filter(
                owner=user, post=obj
            ).first()
            return like.id if like else None
        return None

    class Meta:
        model = Post
        fields = [
            'id', 'OwnerProfile', "OwnerProfileID", 'is_owner', 
            'Profile_image', 'Created_at', 'Updated_at',
            'Title', 'Caption', 'Image', "Tag"
        ]


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = [
            'id', 'TagName', 'Colour'
        ]