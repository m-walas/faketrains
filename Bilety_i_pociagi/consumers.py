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

        seat_number = text_data_json.get('seatNumber')

        # await self.send_reserved_seats(reserved_seats)  #trzeba wysłać które są reserved potem ogarne jak to obsłużyć imo nie ma sensu wysyłać z fronta wszystkich miejsc tylko jedno które potwierdził 
        await self.send(text_data=json.dumps({
            'message': 'Dane odebrane przez serwer',
        }))

    async def send_reserved_seats(self, reserved_seats):
        await self.send(text_data=json.dumps({
            'reservedSeats': reserved_seats,
            'message': 'Reserved seats updated by the server',
        }))
