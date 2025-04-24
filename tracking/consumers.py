# tracking/consumers.py
import json
from channels.generic.websocket import AsyncWebsocketConsumer

class PackageTrackingConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.tracking_id = self.scope['url_route']['kwargs']['tracking_id']
        self.room_group_name = f'track_{self.tracking_id}'

        # Join group
        await self.channel_layer.group_add(self.room_group_name, self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)

    async def receive(self, text_data):
        data = json.loads(text_data)
        latitude = data['latitude']
        longitude = data['longitude']

        # Broadcast location update to group
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'send_location',
                'latitude': latitude,
                'longitude': longitude,
            }
        )

    async def send_location(self, event):
        await self.send(text_data=json.dumps({
            'latitude': event['latitude'],
            'longitude': event['longitude'],
        }))
