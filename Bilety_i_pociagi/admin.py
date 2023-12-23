from django.contrib import admin
from django.contrib.admin import ModelAdmin
from Bilety_i_pociagi.models import Seat
from Bilety_i_pociagi.models import Ticket
from Bilety_i_pociagi.models import Train
from Bilety_i_pociagi.models import Schedule
from Bilety_i_pociagi.models import TrainRoute
from Bilety_i_pociagi.models import Route
from Bilety_i_pociagi.models import TicketPrice
from Bilety_i_pociagi.models import CustomUser
from Bilety_i_pociagi.models import City

from logger import colored_logger as logger

class TicketAdmin(ModelAdmin):
    list_display = ('passenger', 'seat', 'price')


class TrainRouteInline(admin.TabularInline):
    model = Train.routes.through 


@admin.register(Train)
class TrainAdmin(ModelAdmin):
    list_display = ('train_id', 'route', 'travel_time')
    inlines = [TrainRouteInline] 

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

logger.warning("🚀 ~ file: admin.py ~ line 40+ ~ Giving access to admin panel for models: ")
logger.warning("🚀 ~ file: admin.py ~ Train")
logger.warning("🚀 ~ file: admin.py ~ Route")
logger.warning("🚀 ~ file: admin.py ~ TrainRoute")
logger.warning("🚀 ~ file: admin.py ~ Schedule")
logger.warning("🚀 ~ file: admin.py ~ Seat")
logger.warning("🚀 ~ file: admin.py ~ TicketPrice")
logger.warning("🚀 ~ file: admin.py ~ Ticket")
logger.warning("🚀 ~ file: admin.py ~ City")
logger.warning("🚀 ~ file: admin.py ~ CustomUser")
admin.site.register(Route)
admin.site.register(TrainRoute)
admin.site.register(Schedule)
admin.site.register(Seat)
admin.site.register(TicketPrice)
admin.site.register(Ticket)
admin.site.register(City)
admin.site.register(CustomUser)