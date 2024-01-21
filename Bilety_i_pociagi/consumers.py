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

        seat_number = text_data_json['seatNumber']
        is_reserved = text_data_json['isReserved']
        is_confirmed = text_data_json['isConfirmed']

        # Tutaj możesz obsłużyć dane od front-endu, np. zaktualizować stan rezerwacji
        await self.send(text_data=json.dumps({
            'message': 'Dane odebrane przez serwer',
        }))
