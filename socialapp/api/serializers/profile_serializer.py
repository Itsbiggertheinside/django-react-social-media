from rest_framework import serializers
from django.contrib.auth.models import User
from api.models import Profile
from .post_serializer import PostSerializer


class ProfileIsHiddenSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profile
        fields = '__all__'


class ProfileWithPostsSerializer(serializers.ModelSerializer):

    posts = PostSerializer(read_only=True, many=True)

    class Meta:
        model = Profile
        fields = '__all__'


class ProfileUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profile
        exclude = ('slug', 'user', 'picture')


class ProfilePictureUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profile
        fields = ('picture',)