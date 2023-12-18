from django.test import TestCase
from Bilety_i_pociagi.models import Ticket, Seat, Schedule, Train, Route, TicketPrice, CustomUser
from django.contrib.auth import get_user_model
from django.utils import timezone
from datetime import timedelta
from django.urls import reverse

class TicketModelTest(TestCase):
    
    def setUp(self):
        self.passenger = CustomUser.objects.create(first_name='Jan', last_name='Kowalski')
        self.route = Route.objects.create(name='Krakow-Warszawa')
        self.train = Train.objects.create(train_id='EXP001', travel_time="03:00:00", train_type='exp')
        self.train.routes.add(self.route)
        self.seat = Seat.objects.create(train=self.train, number="P01", class_type='first_class')
        self.schedule = Schedule.objects.create(train=self.train, departure_city="Kraków", arrival_city="Warszawa", departure_time="08:00:00", arrival_time="11:00:00")
        TicketPrice.objects.create(train=self.train, route=self.route, price=100)

    def test_ticket_creation(self):
        new_ticket = Ticket.objects.create(
            passenger=self.passenger,
            seat=self.seat,
            schedule=self.schedule,
            valid_date='2020-01-01'
        )

        self.assertIsNotNone(new_ticket.price)
        self.assertEqual(new_ticket.price, 100) 


class CustomUserTests(TestCase):

    def setUp(self):
        self.user = get_user_model()
        self.user = self.user.objects.create(
            username='testuser',
            password='testpass123',
            email = 'test@example.com'
        )
        self.route = Route.objects.create(name='Krakow-Warszawa')
        self.train = Train.objects.create(train_id='EXP001', travel_time="03:00:00", train_type='exp')
        self.train.routes.add(self.route)
        self.seat = Seat.objects.create(train=self.train, number="P01", class_type='first_class')
        self.schedule = Schedule.objects.create(train=self.train, departure_city="Kraków", arrival_city="Warszawa", departure_time="08:00:00", arrival_time="11:00:00")
        TicketPrice.objects.create(train=self.train, route=self.route, price=100)
        
        self.ticket1 = Ticket.objects.create(
            passenger=self.user,
            seat=self.seat,
            schedule=self.schedule,
            valid_date=timezone.now() + timedelta(days=1)
        )
        
        self.ticket2 = Ticket.objects.create(
            passenger=self.user,
            seat=self.seat,
            schedule=self.schedule,
            valid_date=timezone.now() - timedelta(days=1)
        )

    def test_get_tickets(self):
        tickets = self.user.get_tickets()
        self.assertIn(self.ticket1, tickets)
        self.assertIn(self.ticket2, tickets)

    def test_get_past_tickets(self):
        past_tickets = self.user.get_past_tickets()
        self.assertIn(self.ticket2, past_tickets)
        self.assertNotIn(self.ticket1, past_tickets)

    def test_get_future_tickets(self):
        future_tickets = self.user.get_future_tickets()
        self.assertIn(self.ticket1, future_tickets)
        self.assertNotIn(self.ticket2, future_tickets)

    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(
            username='jan',
            email='jan@example.com',
            password='testpass123'
        )
        self.assertEqual(user.username, 'jan')
        self.assertEqual(user.email, 'jan@example.com')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_create_superuser(self):
        User = get_user_model()
        admin_user = User.objects.create_superuser(
            username='superadmin',
            email='superadmin@example.com',
            password='testpass123'
        )
        self.assertEqual(admin_user.username, 'superadmin')
        self.assertEqual(admin_user.email, 'superadmin@example.com')
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)


class TrainSearchTest(TestCase):

    def setUp(self):
        # Tworzenie pociągów
        self.train1 = Train.objects.create(train_id="FT-EXP001", travel_time="03:00:00", train_type="exp")
        self.train2 = Train.objects.create(train_id="FT-EXP002", travel_time="04:00:00", train_type="exp")
        self.train3 = Train.objects.create(train_id="FT-REG001", travel_time="05:00:00", train_type="reg")

        # Tworzenie tras
        self.route1 = Route.objects.create(name="Kraków-Warszawa")
        self.route2 = Route.objects.create(name="Warszawa-Gdańsk")
        self.route3 = Route.objects.create(name="Kraków-Gdańsk")

        # Tworzenie harmonogramów i cen biletów
        self._create_schedules_and_prices()

    def _create_schedules_and_prices(self):
        # Bezpośrednie i pośrednie trasy w różnych scenariuszach
        schedules_data = [
            # Bezpośrednie trasy
            ("FT-EXP001", "Kraków", "08:00:00", "Warszawa", "11:00:00", 100),
            ("FT-EXP002", "Warszawa", "12:00:00", "Gdańsk", "16:00:00", 150),
            # Trasa przekraczająca północ
            ("FT-REG001", "Kraków", "22:00:00", "Warszawa", "03:00:00", 120),
            ("FT-REG001", "Warszawa", "03:30:00", "Gdańsk", "08:30:00", 180),
            # Dłuższy czas oczekiwania na przesiadkę
            ("FT-EXP001", "Warszawa", "14:00:00", "Gdańsk", "18:00:00", 200),
        ]

        for train_id, dep_city, dep_time, arr_city, arr_time, price in schedules_data:
            train = Train.objects.get(train_id=train_id)
            schedule = Schedule.objects.create(
                train=train, departure_city=dep_city, departure_time=dep_time, 
                arrival_city=arr_city, arrival_time=arr_time)
            TicketPrice.objects.create(train=train, route=self.route1, price=price)


    def test_direct_route_search(self):
        response = self.client.get(reverse('search_trains'), {'from': 'Kraków', 'to': 'Warszawa'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Kraków')
        self.assertContains(response, 'Warszawa')

    def test_transfer_route_search(self):
        response = self.client.get(reverse('search_trains'), {'from': 'Kraków', 'to': 'Gdańsk'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Kraków')
        self.assertContains(response, 'Gdańsk')

    def test_no_route_found(self):
        response = self.client.get(reverse('search_trains'), {'from': 'NieistniejąceMiasto', 'to': 'InneNieistniejąceMiasto'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"schedules": []}) 

    def test_direct_route(self):
        response = self.client.get('/search_trains/?from=Kraków&to=Warszawa')
        self.assertIn('FT-EXP001', response.content.decode())

    def test_transfer_route(self):
        response = self.client.get('/search_trains/?from=Kraków&to=Gdańsk')
        self.assertIn('FT-EXP002', response.content.decode())

    # Dodatkowe testy na trudne przypadki
    def test_midnight_cross_route(self):
        response = self.client.get('/search_trains/?from=Kraków&to=Gdańsk')
        self.assertIn('FT-REG001', response.content.decode())  # Trasa przekraczająca północ

    def test_long_wait_transfer(self):
        response = self.client.get('/search_trains/?from=Warszawa&to=Gdańsk')
        self.assertNotIn('FT-EXP001', response.content.decode())  # Długa przesiadka, więc nie powinna się pojawić