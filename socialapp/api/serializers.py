from rest_framework import serializers
from .models import Profile, Post



class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'


class ProfileSerializer(serializers.ModelSerializer):

    post_set = PostSerializer(read_only=True, many=True)

    class Meta:
        model = Profile
        fields = '__all__'
