from rest_framework import serializers
from django.contrib.auth.models import User
from api.models import Profile
from .post_serializer import PostSerializer


class RestAuthUserDetailWithProfileRelated(serializers.ModelSerializer):

    profile = serializers.SlugRelatedField(slug_field='slug', read_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'profile')


class ProfileIsHiddenSerializer(serializers.ModelSerializer):

    username = serializers.SerializerMethodField(read_only=True)
    following_counts = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Profile
        fields = '__all__'

    def get_following_counts(self, obj):
        return {'followers': obj.followinglist.followers.count(), 'followeds': obj.followinglist.followeds.count()}

    def get_username(self, obj):
        return obj.user.username

class ProfileWithPostsSerializer(serializers.ModelSerializer):

    username = serializers.SerializerMethodField(read_only=True)
    posts = PostSerializer(read_only=True, many=True)
    following_counts = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Profile
        fields = '__all__'

    def get_following_counts(self, obj):
        return {'followers': obj.followinglist.followers.count(), 'followeds': obj.followinglist.followeds.count()}

    def get_username(self, obj):
        return obj.user.username

class ProfileUpdateSerializer(serializers.ModelSerializer):

    gender = serializers.CharField(source='get_gender_display')

    class Meta:
        model = Profile
        exclude = ('slug', 'user', 'picture')


class ProfilePictureUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profile
        fields = ('picture',)