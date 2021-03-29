from rest_framework import serializers
from api.models import Message, Profile


class MessageSerializer(serializers.ModelSerializer):

    sender = serializers.SlugRelatedField(slug_field='slug', queryset=Profile.objects.all())
    receiver = serializers.SlugRelatedField(slug_field='slug', queryset=Profile.objects.all())

    class Meta:
        model = Message
        fields = '__all__'


# class DirectChannelSerializer(serializers.ModelSerializer):

#     class Meta:
#         model = DirectChannel
#         fields = '__all__'