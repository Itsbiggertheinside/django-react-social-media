from rest_framework import serializers
from rest_framework.response import Response
from api.models import DirectChannel, Message, Profile


class MessageSerializer(serializers.ModelSerializer):

    sender = serializers.SlugRelatedField(slug_field='slug', queryset=Profile.objects.all())
    username = serializers.CharField(read_only=True, source="sender.user.username")
    picture = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Message
        fields = '__all__'

    def get_picture(self, obj):
        return f'http://127.0.0.1:8000{str(obj.sender.picture.url)}' if obj.sender.picture else None


class DirectChannelSerializer(serializers.ModelSerializer):

    messages = MessageSerializer(read_only=True, many=True)
    creater_info = serializers.SerializerMethodField(read_only=True)
    invited_info = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = DirectChannel
        fields = '__all__'

    def get_creater_info(self, obj):
        return {
            'username': obj.creater.user.username, 
            'picture': 'http://127.0.0.1:8000' + str(obj.creater.picture.url) if obj.creater.picture else None
        }

    def get_invited_info(self, obj):
        return {
            'username': obj.invited.user.username, 
            'picture': 'http://127.0.0.1:8000' + str(obj.invited.picture.url) if obj.invited.picture else None
        }