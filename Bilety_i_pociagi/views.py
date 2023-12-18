import logging
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from .forms import CustomUserCreationForm
from django.http import JsonResponse

from .models import Train, Schedule, TrainRoute, TicketPrice, Route
from datetime import datetime, timedelta

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


def log(*args):

    message = " ".join([str(arg) for arg in args])
    logger.debug(message)


class SignUpView(generic.CreateView):

    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

    def form_valid(self, form):
        response = super().form_valid(form)
        print("Form is valid. Redirecting to login page.")
        return response
    
    def form_invalid(self, form):
        response = super().form_invalid(form)
        print("Form is invalid. Rendering form with errors.")
        print(form.errors)
        return response


def index(request):
    return render(request, 'index.html')


def search_trains(request):

    from_station = request.GET.get('from').lower()
    to_station = request.GET.get('to').lower()

    log("🚀 ~ file: views.py ~ Searching trains from", from_station, "to", to_station)

    direct_schedules = get_direct_schedules(from_station, to_station)

    transfer_routes = get_transfer_routes(from_station, to_station)

    schedules_data = direct_schedules + transfer_routes

    return JsonResponse({"schedules": schedules_data})


def get_direct_schedules(from_station, to_station):

    direct_routes = TrainRoute.objects.filter(
        route__name__istartswith=from_station, route__name__iendswith=to_station)

    direct_schedules = Schedule.objects.filter(
        train__in=[route.train for route in direct_routes],
        departure_city__istartswith=from_station,
        arrival_city__iendswith=to_station,
    )
    # log("🚀 ~ file: views.py:65 ~ direct_schedules:", direct_schedules)
    return [get_schedule_data(schedule) for schedule in direct_schedules]


# function to check if transfer is sensible using geo coordinates of cities
def is_sensible_transfer(from_city, intermediate_city, to_city):
    
    from_city = from_city.lower()
    intermediate_city = intermediate_city.lower()
    to_city = to_city.lower()

    # TODO:
    return True


def calculate_time_difference(time1, time2):

    datetime1 = datetime.combine(datetime.today(), time1)
    datetime2 = datetime.combine(datetime.today(), time2)

    if time2 < time1:
        datetime2 += timedelta(days=1)

    difference = datetime2 - datetime1
    return difference.total_seconds() / 60


def get_transfer_routes(from_station, to_station, max_wait_time=120):
    transfer_routes = []

    intermediate_cities = Schedule.objects.filter(
        departure_city__iexact=from_station
    ).exclude(arrival_city__iexact=to_station).values_list('arrival_city', flat=True).distinct()
    
    for intermediate_city in intermediate_cities:
        if not is_sensible_transfer(from_station, intermediate_city, to_station):
            continue

        first_legs = Schedule.objects.filter(
            departure_city__iexact=from_station, arrival_city__iexact=intermediate_city
        )

        second_legs = Schedule.objects.filter(
            departure_city__iexact=intermediate_city, arrival_city__iexact=to_station
        )

        for first_leg in first_legs:
            for second_leg in second_legs:
                if second_leg.departure_time > first_leg.arrival_time:
                    wait_time_minutes = calculate_time_difference(first_leg.arrival_time, second_leg.departure_time)

                    if wait_time_minutes <= max_wait_time:
                        transfer_route_data = {
                            "first_leg": get_schedule_data(first_leg, is_transfer=True),
                            "second_leg": get_schedule_data(second_leg, is_transfer=True),
                        }
                        transfer_routes.append(transfer_route_data)

    return transfer_routes


def get_schedule_data(schedule, is_transfer=False):
    
    train = schedule.train    

    try:
        route = Route.objects.get(name__contains=f"{schedule.departure_city}-{schedule.arrival_city}")
        ticket_price = TicketPrice.objects.get(train=train, route=route).price
    except (TicketPrice.DoesNotExist, Route.DoesNotExist):
        ticket_price = "N/A"

    # ! schedules data in json format :
    schedule_data = {
        "train_id": schedule.train.train_id,
        "departure_city": schedule.departure_city,
        "departure_time": schedule.departure_time.strftime('%H:%M:%S'),
        "arrival_city": schedule.arrival_city,
        "arrival_time": schedule.arrival_time.strftime('%H:%M:%S'),
        "ticket_price": str(ticket_price),
        "travel_time": Train.objects.get(train_id=schedule.train.train_id).travel_time,
        "is_transfer": is_transfer,
    }

    return schedule_data

    # todo: filter schedules
