from django.test import TestCase
from Bilety_i_pociagi.models import Ticket, Passenger, Seat, Schedule, Train, Route, TicketPrice

class TicketModelTest(TestCase):
    
    def setUp(self):
        self.passenger = Passenger.objects.create(first_name='Jan', last_name='Kowalski')
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
