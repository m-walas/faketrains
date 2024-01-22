# myapp/serializers.py
from rest_framework import serializers
from .models import Ticket

class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = ['id', 'passenger', 'seat', 'valid_date', 'schedule', 'price', 'status']
