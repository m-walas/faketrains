# myapp/serializers.py
from rest_framework import serializers
from .models import Ticket

class TicketSerializer(serializers.ModelSerializer):
    departure_city = serializers.SerializerMethodField()
    arrival_city = serializers.SerializerMethodField()
    seat_number = serializers.SerializerMethodField()
    train_name = serializers.SerializerMethodField()
    departure_time = serializers.SerializerMethodField()

    class Meta:
        model = Ticket
        fields = ['id', 'passenger', 'valid_date', 'price', 'status',
                  'departure_city', 'arrival_city', 'departure_time', 'seat_number', 'train_name']

    def get_departure_city(self, obj):
        return obj.schedule.departure_city

    def get_arrival_city(self, obj):
        return obj.schedule.arrival_city

    def get_departure_time(self, obj):
        return obj.schedule.departure_time.strftime("%H:%M:%S") if obj.schedule.departure_time else None

    def get_seat_number(self, obj):
        return obj.seat.number if obj.seat else None

    def get_train_name(self, obj):
        return obj.seat.train.train_id if obj.seat else None