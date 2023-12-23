from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
import datetime

class CustomUser(AbstractUser):
    def get_tickets(self):
        return self.ticket_set.all()
    
    def get_past_tickets(self):
        return self.ticket_set.filter(valid_date__lt=datetime.date.today())
    
    def get_future_tickets(self):
        return self.ticket_set.filter(valid_date__gte=datetime.date.today())


class City(models.Model):
    name = models.CharField(max_length=100)
    geo_latitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    geo_longitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)

    def __str__(self):
        return self.name + f" ({self.geo_longitude}, {self.geo_latitude})"


class Route(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Train(models.Model):
    train_id = models.CharField(max_length=100, unique=True)
    # travel_time is in format 03:00:00 and different for each train
    travel_time = models.CharField(max_length=2+1+2+1+2)
    train_type = models.CharField(
        max_length=3,
        choices=[
            ('exp', 'Expresowy'),
            ('reg', 'Regionalny'),
        ]
    )
    routes = models.ManyToManyField(Route, through='TrainRoute')

    def __str__(self):
        return self.train_id


class TrainRoute(models.Model):
    train = models.ForeignKey(Train, on_delete=models.CASCADE)
    route = models.ForeignKey(Route, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.train} - {self.route}"


class Schedule(models.Model):
    train = models.ForeignKey(Train, on_delete=models.CASCADE) 
    departure_city = models.CharField(max_length=100) 
    departure_time = models.TimeField()  
    arrival_city = models.CharField(max_length=100)  
    arrival_time = models.TimeField() 

    def __str__(self):
        return f"{self.train} {self.departure_time} {self.departure_city} -> {self.arrival_time} {self.arrival_city}"


class Seat(models.Model):
    TRAIN_CLASS_CHOICES = (
        ('first_class', 'Pierwsza klasa'),
        ('second_class', 'Druga klasa'),
    )

    train = models.ForeignKey(Train, on_delete=models.CASCADE)
    number = models.CharField(max_length=10, blank=False, null=False)
    class_type = models.CharField(max_length=20, choices=TRAIN_CLASS_CHOICES, default='second_class')

    def __str__(self):
        return f"Miejsce {self.number} - {self.train} ({self.get_class_type_display()})"


class TicketPrice(models.Model):
    train = models.ForeignKey(Train, on_delete=models.CASCADE)
    route = models.ForeignKey(Route, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return f"{self.train} na trasie {self.route} - Cena: {self.price} zł"


class Ticket(models.Model):
    STATUS_CHOICES = (
        ('reserved', 'Zarezerwowany'),
        ('confirmed', 'Kupiony'),
    )

    passenger = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    seat = models.ForeignKey(Seat, on_delete=models.CASCADE)
    valid_date = models.DateField()
    schedule = models.ForeignKey(Schedule, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='available')

    def save(self, *args, **kwargs):
        if not self.pk:
            ticket_price = TicketPrice.objects.get(
                train=self.schedule.train,
                route=self.schedule.train.trainroute_set.first().route
            )
            self.price = ticket_price.price
        super().save(*args, **kwargs)

    def __str__(self):
        train = self.seat.train
        route = train.trainroute_set.first().route
        return f"Bilet {self.id} - {self.passenger} - Miejsce: {self.seat} - Trasa: {self.schedule.train} {self.schedule.departure_city} -> {self.schedule.arrival_city} - Data i godzina odjazdu: {self.schedule.departure_time} - Ważny w: {self.valid_date} - Status: {self.get_status_display()}"

    # !TODO: podczas kupowania biletu, w miejscu formularza gdzie się będzie wypełniało dane, zadbać o to, żeby 
    # !nie można było wybrać miejsca pociagu, który nie kursuje na danej trasie
    # !teraz jest tak:
    # !Bilet 1 - Mateusz Walas - Miejsce: Miejsce 001-PR - FT-EXP001 (Pierwsza klasa) 
    # !- Trasa: FT-EXP005 Warszawa -> Gdańsk - Data i godzina odjazdu: 10:00:00 
    # !- Ważny w: 2023-12-03 - Status: Zarezerwowany
    # !Miejsce 001-PR to miejsce z pociągu FT-EXP001, który nie kursuje na trasie FT-EXP005 Warszawa -> Gdańsk
