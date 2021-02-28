from rest_framework import serializers
from .models import Profile, Post



class PostSerializer(serializers.ModelSerializer):

    user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Post
        fields = '__all__'


class ProfileSerializer(serializers.ModelSerializer):

    user = serializers.StringRelatedField(read_only=True)
    picture = serializers.ImageField(read_only=True)
    post_set = PostSerializer(read_only=True, many=True)

    class Meta:
        model = Profile
        fields = '__all__'


class ProfilePhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('image',)