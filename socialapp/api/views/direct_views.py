from rest_framework import viewsets
from rest_framework.response import Response
from api.serializers import MessageSerializer
from api.models import Message



class DirectViewSet(viewsets.ModelViewSet):
    serializer_class = MessageSerializer

    def get_queryset(self):
        if self.action == 'receive':
            return Message.objects.filter(sender__user=self.kwargs.get('username'))
        return Response({'bla': 'bla bla bla'})