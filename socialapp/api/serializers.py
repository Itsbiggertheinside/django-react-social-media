from rest_framework import serializers
from .models import Profile, Post, Comment, Follow



class FollowSerializer(serializers.ModelSerializer):

    followers_list = serializers.SerializerMethodField()
    followeds_list = serializers.SerializerMethodField()

    class Meta:
        model = Follow
        exclude = ('id',)

    def get_followers_list(self, instance):
        return list(instance.followers_list.values_list('slug', flat=True))

    def get_followeds_list(self, instance):
        return list(instance.followeds_list.values_list('slug', flat=True))


class CommentSerializer(serializers.ModelSerializer):

    user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Comment
        exclude = ('id', 'post',)


class PostSerializer(serializers.ModelSerializer):

    user = serializers.StringRelatedField(read_only=True)
    comment_set = CommentSerializer(read_only=True, many=True)

    class Meta:
        model = Post
        fields = '__all__'


class ProfileSerializer(serializers.ModelSerializer):

    user = serializers.StringRelatedField(read_only=True)
    picture = serializers.ImageField(read_only=True)
    post_set = PostSerializer(read_only=True, many=True)
    follow_set = FollowSerializer(read_only=True, many=True)

    class Meta:
        model = Profile
        fields = '__all__'


class ProfilePhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('image',)
