from django.db import models

# Create your models here.


class Train(models.Model):
    name = models.CharField(max_length=100) # nazwa pociągu
    departure_station = models.CharField(max_length=100) # stacja początkowa
    arrival_station = models.CharField(max_length=100) # stacja końcowa
    departure_time = models.DateTimeField() # czas odjazdu
    arrival_time = models.DateTimeField() # czas przyjazdu
    price = models.DecimalField(max_digits=10, decimal_places=2) # cena biletu


class Seat(models.Model):
    train = models.ForeignKey(Train, on_delete=models.CASCADE) # pociąg
    seat_number = models.CharField(max_length=10) # numer miejsca
    status = models.CharField(max_length=1
                            , choices=[('f', 'free'), ('r', 'reserved'), ('b', 'bought')]
                            , default='f') # status miejsca (wolne, zarezerwowane, kupione

    def __str__(self):
        return f"{self.train.name} {self.seat_number} {self.status}"


class Passenger(models.Model):
    first_name = models.CharField(max_length=50) # imię
    last_name = models.CharField(max_length=50) # nazwisko
    email = models.EmailField() # adres email
    phone = models.CharField(max_length=9) # numer telefonu


class Ticket(models.Model):
    train = models.ForeignKey(Train, on_delete=models.CASCADE) # pociąg
    passenger = models.ForeignKey(Passenger, on_delete=models.CASCADE) # pasażer

    seat_number = models.CharField(max_length=10) # numer miejsca
    is_confirmed = models.BooleanField(default=False) # czy bilet został potwierdzony
    purchase_date = models.DateTimeField(auto_now_add=True) # data zakupu
