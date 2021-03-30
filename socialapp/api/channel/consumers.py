import json
from channels.generic.websocket import AsyncWebsocketConsumer

class DirectConsumer(AsyncWebsocketConsumer):

    async def connect(self):
        self.direct_code = self.scope['url_route']['kwargs']['direct_code']
        self.direct_group_code = 'direct_%s' % self.direct_code

        await self.channel_layer.group_add(
            self.direct_group_code, self.channel_name
        )
        
        await self.accept()

    async def disconnect(self, close_code):
        
        await self.channel_layer.group_discard(
            self.direct_group_code, self.channel_name
        )

    async def receive(self, text_data=None):
        text_data_json = json.loads(text_data)
        username = text_data_json['username']
        message = text_data_json['message']

        await self.channel_layer.group_send(
            self.direct_group_code, {
                'type': 'direct_channel_message',
                'username': username,
                'message': message
            }
        )

    async def direct_channel_message(self, event):
        username = event['username']
        message = event['message']

        await self.send(text_data=json.dumps({
            'username': username,
            'message': message
        }))