from rest_framework import serializers
from api.models import Post, Likes, Comment, Followed


class LikesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Likes
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = '__all__'


class PostSerializer(serializers.ModelSerializer):

    owner = serializers.SerializerMethodField(read_only=True)
    likes_set = LikesSerializer(read_only=True, many=True)
    comment_set = CommentSerializer(read_only=True, many=True)

    class Meta:
        model = Post
        fields = '__all__'

    def get_owner(self, obj):
        return {'username': obj.profile.user.username, 'picture': 'http://127.0.0.1:8000/media/' + str(obj.profile.picture)}
