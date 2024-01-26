import json
from channels.generic.websocket import AsyncWebsocketConsumer
from logger import colored_logger as logger

class TrainSeatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        logger.info("🚀 WEBSOCKET CONNECTED 🚀 ")
        await self.accept()

    async def disconnect(self, close_code):
        logger.warn(f" ❌ WebSocket disconnected with code: {close_code} ❌ ")
        pass

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)

        selected_seat_numbers = text_data_json.get('selectedSeatNumbers', [])

        # reserved_seats = #z backendu dostać i wysłać najlepiej jako lista [1, 2, 6, 9] tak jak dostaje selectedSeatNumbers

        # response_data = {
        #     'message': 'Seats confirmed by the server',
        #     'reservedSeats': reserved_seats,
        # }

        # await self.send(text_data=json.dumps(response_data))
