from rest_framework import serializers
from api.models import Post, Likes, Comment


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
            likes.append(like.profile.user.username)
        return likes
