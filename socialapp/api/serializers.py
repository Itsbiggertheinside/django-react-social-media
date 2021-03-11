from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Profile, Post, Likes, Comment, ArchivedPost, Follows, Following


class FollowsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Follows
        fields = '__all__'


class FollowingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Following
        fields = '__all__'


class LikesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Likes
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = '__all__'


class PostSerializer(serializers.ModelSerializer):

    likes_set = serializers.SerializerMethodField(read_only=True)
    comment_set = CommentSerializer(read_only=True, many=True)

    class Meta:
        model = Post
        fields = '__all__'

    def get_likes_set(self, obj):
        likes = []
        for like in obj.likes_set.all():
            likes.append(like.profile.slug)
        return likes


class ProfileSerializer(serializers.ModelSerializer):

    posts = PostSerializer(read_only=True, many=True)

    class Meta:
        model = Profile
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):

    profile = ProfileSerializer()

    class Meta:
        model = User
        fields = ('username', 'profile')