from dj_rest_auth.serializers import UserDetailsSerializer
from rest_framework import serializers
from profiles.models import Profile
from collection.models import Collections


class CurrentUserSerializer(UserDetailsSerializer):
    profile_id = serializers.ReadOnlyField(source='profile.id')
    profile_image = serializers.ReadOnlyField(source='profile.ProfileImage.url')
    collection_id = serializers.SerializerMethodField()

    def get_collection_id(self, obj):
        profile = Profile.objects.filter(User=obj).first()
        collection = Collections.objects.filter(Profile=profile).first()
        return collection.id if collection is not None else ""

    class Meta(UserDetailsSerializer.Meta):
        fields = UserDetailsSerializer.Meta.fields + (
            'profile_id', 'profile_image', "collection_id"
        )
