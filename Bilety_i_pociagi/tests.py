from django.test import TestCase
from Bilety_i_pociagi.models import Ticket, Seat, Schedule, Train, Route, TicketPrice, CustomUser
from django.contrib.auth import get_user_model
from django.utils import timezone
from datetime import timedelta

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
