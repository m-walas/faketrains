from django.contrib import admin

from django.contrib import admin
from django.contrib.admin import ModelAdmin
from Bilety_i_pociagi.models import Seat
from Bilety_i_pociagi.models import Ticket
from Bilety_i_pociagi.models import Train
from Bilety_i_pociagi.models import Passenger


class TicketAdmin(ModelAdmin):
    list_display = ('train', 'passenger', 'seat_number', 'is_confirmed', 'purchase_date')


admin.site.register(Ticket, TicketAdmin)
admin.site.register(Train)
admin.site.register(Passenger)
admin.site.register(Seat)
