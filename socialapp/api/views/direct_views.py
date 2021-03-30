from rest_framework import viewsets, mixins, generics
from rest_framework.response import Response
from api.serializers import DirectChannelSerializer, MessageSerializer
from api.models import DirectChannel, Message, Profile
# from api.permissions import IsChannelMemberOrAccessDenied



class DirectChannelViewSet(viewsets.ModelViewSet):
    serializer_class = DirectChannelSerializer
    # permission_classes = (IsChannelMemberOrAccessDenied, )

    def get_queryset(self):
        queryset = DirectChannel.objects.all()

        if self.action == 'list':
            return queryset.filter(creater=self.request.user.profile) | queryset.filter(invited=self.request.user.profile)

        return queryset

class DirectMessageCreateViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer