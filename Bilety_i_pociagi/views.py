from django.shortcuts import render
from django.urls import reverse_lazy, get_resolver
from django.views import generic
from django.contrib.auth import login, authenticate, logout
from .forms import CustomUserCreationForm
from django.http import JsonResponse
from datetime import datetime, timedelta
from math import radians, cos, sin, sqrt, atan2
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny
from rest_framework.decorators import api_view, permission_classes
from django.views.decorators.http import require_POST
import json
import datetime as dt

from .models import Train, Schedule, TrainRoute, TicketPrice, Route, City, Seat, Ticket
from .serializers import CitySerializer

from logger import colored_logger as logger

# ! backup - do not delete
# @api_view(['POST'])
# def login_view(request):
#     username = request.data.get('username')
#     password = request.data.get('password')
#     user = authenticate(username=username, password=password)
#     if user is not None:
#         login(request, user)
#         return JsonResponse({"success": True, "firstName": user.first_name, "lastName": user.last_name, "username": user.username})
#     else:
#         return JsonResponse({"success": False, "error": "Błędne dane logowania"}, status=401)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def user_profile(request):
    user = request.user
    return Response({
        "firstName": user.first_name,
        "lastName": user.last_name,
    })


@api_view(['POST'])
def logout_view(request):
    logout(request)
    return JsonResponse({"success": True})


@api_view(['POST'])
@permission_classes([AllowAny])
def register_view(request):
    form = CustomUserCreationForm(request.data)

    if form.is_valid():
        form.save()
        return JsonResponse({"success": True})
    else:
        return JsonResponse({"success": False, "error": form.errors.as_json()}, status=400)


@api_view(['GET'])
def user_status(request):
    if request.user.is_authenticated:
        logger.debug(f"🚀 ~ file: views.py ~ user_status ~ request.user: {request.user}")
        return JsonResponse({"isLoggedIn": True, "firstName": request.user.first_name, "lastName": request.user.last_name})
    return JsonResponse({"isLoggedIn": False})


class ListAPIEndpoints(APIView):
    permission_classes = [IsAdminUser]

    def get(self, request, format=None):
        urlconf = get_resolver()
        all_urls = list()
        for url_pattern in urlconf.url_patterns:
            all_urls.append(url_pattern.pattern.describe())
        return Response(all_urls)


class SignUpView(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

    def form_valid(self, form):
        response = super().form_valid(form)
        logger.debug("Form is valid. Redirecting to login page.")
        return response
    
    def form_invalid(self, form):
        response = super().form_invalid(form)
        logger.error("Form is invalid. Rendering form with errors.")
        logger.error(form.errors)
        return response


class CitySearchView(APIView):
    def get(self, request):
        query = request.query_params.get('search', '')
        cities = City.objects.filter(name__istartswith=query)
        serializer = CitySerializer(cities, many=True)
        return Response(serializer.data)


@require_POST
def receive_selected_route(request):
    try:
        data = json.loads(request.body)
        train_id = data.get('train_id')
        departure_time = data.get('departure_time')
        departure_date = data.get('departure_date')
        departure_city = data.get('departure_city')
        arrival_city = data.get('arrival_city')

        logger.debug(f"🚀 ~ file: views.py ~ receive_selected_route ~ route selected from frontend: ")
        logger.debug(f"🚀 ~ file: views.py ~ train_id: {train_id}")
        logger.debug(f"🚀 ~ file: views.py ~ departure_time: {departure_time}")

        return JsonResponse({"status": "success", "message": "Trasa odebrana"})
    except json.JSONDecodeError:
        logger.error("❌ JSONDecodeError ❌")
        return JsonResponse({"status": "error", "message": "Nieprawidłowe dane"}, status=400)


def get_train_seats_with_availability(request, train_id, departure_date, departure_time):
    try:
        departure_date = dt.datetime.strptime(departure_date, '%Y-%m-%d').date()
        departure_time = dt.datetime.strptime(departure_time, '%H:%M:%S').time()

        train = Train.objects.get(train_id=train_id)
        schedule = Schedule.objects.get(train=train, departure_time=departure_time)

        seats = Seat.objects.filter(train=train)
        seats_data = []
        for seat in seats:
            ticket_exists = Ticket.objects.filter(seat=seat, valid_date=departure_date, schedule=schedule).exists()
            seats_data.append({
                "seat_number": seat.number,
                "class_type": seat.class_type,
                "is_available": not ticket_exists
            })

        logger.info(f"🚀 ~ file: views.py ~ get_train_seats_with_availability ~ zwrócono miejsca")
        return JsonResponse({"seats": seats_data})
    except Train.DoesNotExist:
        logger.error("❌ Train.DoesNotExist ❌")
        return JsonResponse({"error": "Pociąg nie istnieje"}, status=404)
    except Schedule.DoesNotExist:
        logger.error("❌ Schedule.DoesNotExist ❌")
        return JsonResponse({"error": "Harmonogram nie istnieje"}, status=404)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)


def index(request):
    return render(request, 'index.html')


def search_trains(request):

    from_station = request.GET.get('from').lower()
    to_station = request.GET.get('to').lower()

    logger.debug(f"🚀 ~ file: views.py ~ Searching trains from {from_station} to {to_station}")

    direct_schedules = get_direct_schedules(from_station, to_station)

    transfer_routes = get_transfer_routes(from_station, to_station)

    schedules_data = direct_schedules + transfer_routes

    return JsonResponse({"schedules": schedules_data})


def get_direct_schedules(from_station, to_station):

    logger.debug(f"🚀 ~ file: views.py ~ get_direct_schedules ~ from_station: {from_station}")

    direct_routes = TrainRoute.objects.filter(
        route__name__istartswith=from_station, route__name__iendswith=to_station)

    direct_schedules = Schedule.objects.filter(
        train__in=[route.train for route in direct_routes],
        departure_city__istartswith=from_station,
        arrival_city__iendswith=to_station,
    )
    # logger.info(f"🚀 ~ file: views.py ~ get_direct_schedules ~ direct_schedules: {direct_schedules}")
    return [get_schedule_data(schedule) for schedule in direct_schedules]


# function to check if transfer is sensible using geo coordinates of cities
def is_sensible_transfer(from_city, intermediate_city, to_city):
    
    logger.debug(f"🚀 ~ file: views.py ~ Checking if transfer from {from_city} to {to_city} via {intermediate_city} is sensible")

    from_city = from_city.lower()
    intermediate_city = intermediate_city.lower()
    to_city = to_city.lower()

    #* with func haversine we can calculate distance between two points on earth surface
    #* and we can check if transfer is sensible by the distance between cities
    def haversine(lat1, lon1, lat2, lon2):
        R = 6371 # Earth radius in kilometers

        lat1, lon1, lat2, lon2 = map(radians, [lat1, lon1, lat2, lon2])

        dlat = lat2 - lat1
        dlon = lon2 - lon1

        a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
        c = 2 * atan2(sqrt(a), sqrt(1-a))

        distance = R * c

        return distance
    
    #? getting geo coordinates of cities
    from_city_coordinates = City.objects.get(name__iexact=from_city)
    logger.info(f"🚀 ~ file: views.py ~ is_sensible_transfer ~ {from_city} coordinates: {from_city_coordinates}")
    intermediate_city_coordinates = City.objects.get(name__iexact=intermediate_city)
    logger.info(f"🚀 ~ file: views.py ~ is_sensible_transfer ~ {intermediate_city} coordinates: {intermediate_city_coordinates}")
    to_city_coordinates = City.objects.get(name__iexact=to_city)
    logger.info(f"🚀 ~ file: views.py ~ is_sensible_transfer ~ {to_city} coordinates: {to_city_coordinates}")

    #? calculating distance between cities
    distance_from_to = haversine(from_city_coordinates.geo_latitude, from_city_coordinates.geo_longitude, to_city_coordinates.geo_latitude, to_city_coordinates.geo_longitude)
    logger.info(f"🚀 ~ file: views.py ~ is_sensible_transfer ~ distance from {from_city} to {to_city}: {distance_from_to}")
    distance_from_intermediate = haversine(from_city_coordinates.geo_latitude, from_city_coordinates.geo_longitude, intermediate_city_coordinates.geo_latitude, intermediate_city_coordinates.geo_longitude)
    logger.info(f"🚀 ~ file: views.py ~ is_sensible_transfer ~ distance from {from_city} to {intermediate_city}: {distance_from_intermediate}")
    distance_intermediate_to = haversine(intermediate_city_coordinates.geo_latitude, intermediate_city_coordinates.geo_longitude, to_city_coordinates.geo_latitude, to_city_coordinates.geo_longitude)
    logger.info(f"🚀 ~ file: views.py ~ is_sensible_transfer ~ distance from {intermediate_city} to {to_city}: {distance_intermediate_to}")

    #? if dist from-intermediate-to is less +100km than dist from-to, then transfer is sensible
    if distance_from_intermediate + distance_intermediate_to < distance_from_to + 100:
        logger.debug(f"🚀 ~ file: views.py ~ is_sensible_transfer ~ transfer from {from_city} to {to_city} via {intermediate_city} is sensible")
        return True
    else:
        logger.warning(f"❗ transfer from {from_city} to {to_city} via {intermediate_city} is not sensible ❗")
        return False


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
            logger.critical("❌ Transfer is not sensible because of the distance. Skipping... ❌")
            continue

        first_legs = Schedule.objects.filter(
            departure_city__iexact=from_station, arrival_city__iexact=intermediate_city
        )

        second_legs = Schedule.objects.filter(
            departure_city__iexact=intermediate_city, arrival_city__iexact=to_station
        )

        logged = False

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
                        logger.warning(f"✔️ Transfer at {second_leg.departure_time} is sensible. Adding to transfer_routes... ✔️")
                    elif (not logged) and (wait_time_minutes > max_wait_time):
                        logged = True
                        logger.critical(f"❌ Transfer at {second_leg.departure_time} is not sensible because of the waiting time. Skipping... ❌")

    return transfer_routes


def get_schedule_data(schedule, is_transfer=False):

    # logger.info(f"🚀 ~ file: views.py ~ get_schedule_data ~ schedule: {schedule}")

    train = schedule.train    

    try:
        route = Route.objects.get(name__contains=f"{schedule.departure_city}-{schedule.arrival_city}")
        ticket_price = TicketPrice.objects.get(train=train, route=route).price
    except (TicketPrice.DoesNotExist, Route.DoesNotExist):
        ticket_price = "N/A"

    #! schedules data in json format :
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
