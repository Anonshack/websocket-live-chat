import json
from channels.generic.websocket import AsyncWebsocketConsumer
from datetime import datetime


class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = f'chat_{self.room_name}'

        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        await self.accept()

        # Xonaga ulanganlik haqida xabar
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'system_message',
                'message': f"Yangi foydalanuvchi ulandi 👋",
            }
        )

    async def disconnect(self, close_code):
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'system_message',
                'message': "Foydalanuvchi chiqdi 👋",
            }
        )
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        data = json.loads(text_data)
        message = data.get('message', '').strip()
        username = data.get('username', 'Anonim')

        if not message:
            return

        now = datetime.now().strftime('%H:%M')

        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message,
                'username': username,
                'time': now,
                'channel': self.channel_name,
            }
        )

    async def chat_message(self, event):
        await self.send(text_data=json.dumps({
            'type': 'message',
            'message': event['message'],
            'username': event['username'],
            'time': event['time'],
            'is_me': event['channel'] == self.channel_name,
        }))

    async def system_message(self, event):
        await self.send(text_data=json.dumps({
            'type': 'system',
            'message': event['message'],
        }))
