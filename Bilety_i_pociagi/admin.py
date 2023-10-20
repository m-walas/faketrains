from django.contrib import admin
from django.contrib.admin import ModelAdmin
from Bilety_i_pociagi.models import Seat
from Bilety_i_pociagi.models import Ticket
from Bilety_i_pociagi.models import Train
from Bilety_i_pociagi.models import Passenger
from Bilety_i_pociagi.models import Schedule
from Bilety_i_pociagi.models import TrainRoute
from Bilety_i_pociagi.models import Route


class TicketAdmin(ModelAdmin):
    list_display = ('passenger', 'seat', 'price')


# Definicja inline modelu dla TrainRoute
class TrainRouteInline(admin.TabularInline):
    model = Train.routes.through  # Użyj modelu pośredniczącego


# Definicja panelu admina dla modelu Train
@admin.register(Train)
class TrainAdmin(admin.ModelAdmin):
    list_display = ('train_id', 'route', 'travel_time')
    inlines = [TrainRouteInline]  # Dodaj inline model TrainRouteInline

    def train_id(self, obj):
        return obj.train_id

    def route(self, obj):
        return obj.routes.all()

    def travel_time(self, obj):
        return obj.travel_time

    def get_inline_instances(self, request, obj=None):
        if not obj:
            return list()
        return super(TrainAdmin, self).get_inline_instances(request, obj)


admin.site.register(TrainRoute)
admin.site.register(Seat)
admin.site.register(Passenger)
admin.site.register(Route)
admin.site.register(Schedule)
admin.site.register(Ticket)
