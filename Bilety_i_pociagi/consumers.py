import json
from channels.generic.websocket import AsyncWebsocketConsumer

class TrainSeatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        print("WebSocket connected")
        await self.accept()

    async def disconnect(self, close_code):
        print(f"WebSocket disconnected with code: {close_code}")
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
