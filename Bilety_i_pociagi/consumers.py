import json
from channels.generic.websocket import AsyncWebsocketConsumer
from logger import colored_logger as logger

class TrainSeatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = 'train_seats'
        self.room_group_name = f"chat_{self.room_name}"

        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        logger.info("🚀 WEBSOCKET CONNECTED 🚀 ")
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

        logger.warn(f" ❌ WebSocket disconnected with code: {close_code} ❌ ")
        pass

    async def receive(self, text_data):
        data_json = json.loads(text_data)
        seat_info = data_json['seat_info']

        # Send seat_info to room group
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'seat_info',
                'seat_info': seat_info
            }
        )

    async def seat_info(self, event):
        seat_info = event['seat_info']

        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'seat_info': seat_info
        }))
