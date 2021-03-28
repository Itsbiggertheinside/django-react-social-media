from rest_framework import serializers
from api.models import FollowingList, Follower, Followed
from .profile_serializer import ProfileWithPostsSerializer


class FollowersSerializer(serializers.ModelSerializer):

    username = serializers.SerializerMethodField()
    picture = serializers.SerializerMethodField()

    class Meta:
        model = Follower
        fields = '__all__'

    def get_username(self, obj):
        return obj.follower.user.username

    def get_picture(self, obj):
        return 'http://127.0.0.1:8000' + obj.follower.picture.url if obj.follower.picture else None


class FollowedsSerializer(serializers.ModelSerializer):

    username = serializers.SerializerMethodField()
    picture = serializers.SerializerMethodField()

    class Meta:
        model = Followed
        fields = '__all__'

    def get_username(self, obj):
        return obj.followed.user.username

    def get_picture(self, obj):
        return 'http://127.0.0.1:8000' + obj.followed.picture.url if obj.followed.picture else None


class FollowingListSerializer(serializers.ModelSerializer):

    followers = FollowersSerializer(read_only=True, many=True)
    followeds = FollowedsSerializer(read_only=True, many=True)

    class Meta:
        model = FollowingList
        fields = '__all__'


class FollowedProfilesPosts(serializers.ModelSerializer):

    followed = ProfileWithPostsSerializer(read_only=True)
    
    class Meta:
        model = Followed
        fields = ('followed',)