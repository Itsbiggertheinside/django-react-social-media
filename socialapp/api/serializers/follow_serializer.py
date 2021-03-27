from rest_framework import serializers
from api.models import FollowingList, Follower, Followed
from .profile_serializer import ProfileWithPostsSerializer


class FollowersSerializer(serializers.ModelSerializer):

    class Meta:
        model = Follower
        fields = '__all__'


class FollowedsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Followed
        fields = '__all__'


class FollowingListSerializer(serializers.ModelSerializer):

    followers = serializers.SerializerMethodField(read_only=True)
    followeds = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = FollowingList
        fields = '__all__'

    def get_followers(self, obj):
        return obj.followers.values('id', 'follower_id', 'follower_id__user__username')

    def get_followeds(self, obj):
        return obj.followeds.values('id', 'followed_id', 'followed_id__user__username')


class FollowedProfilesPosts(serializers.ModelSerializer):

    followed = ProfileWithPostsSerializer(read_only=True)
    
    class Meta:
        model = Followed
        fields = ('followed',)