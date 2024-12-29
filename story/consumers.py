import json
from channels.generic.websocket import AsyncWebsocketConsumer

class SceneConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.title = self.scope['url_route']['kwargs']['title']
        self.chapter_number = self.scope['url_route']['kwargs']['chapter_number']
        self.room_group_name = f'scene_updates_{self.title}_{self.chapter_number}'

        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )
