from django.db import models


class Route(models.Model):
    name = models.CharField(max_length=100, unique=True, blank=False, null=False)

    def __str__(self):
        return self.name


class TrainRoute(models.Model):
    train = models.ForeignKey('Train', on_delete=models.CASCADE)
    route = models.ForeignKey(Route, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.train} - {self.route}"


class Train(models.Model):
    train_id = models.CharField(max_length=100, unique=True, blank=False, null=False)
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


class Schedule(models.Model):
    train = models.ForeignKey(Train, on_delete=models.CASCADE)  # Połączenie z pociągiem
    departure_city = models.CharField(max_length=100)  # Miasto odjazdu
    departure_time = models.TimeField()  # Godzina odjazdu
    arrival_city = models.CharField(max_length=100)  # Miasto przyjazdu
    arrival_time = models.TimeField()  # Godzina przyjazdu

    def __str__(self):
        return f"{self.train} {self.departure_city} -> {self.arrival_city}"


class Passenger(models.Model):
    # all fields are required
    first_name = models.CharField(max_length=100, blank=False, null=False)
    last_name = models.CharField(max_length=100, blank=False, null=False)
    email = models.EmailField(max_length=254, blank=False, null=False, unique=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Seat(models.Model):
    """
    Model reprezentujący miejsce w pociągu.

    Pola:
    - train: pociąg, do którego przypisane jest miejsce.
    - number: numer miejsca (np. 23A).
    - class_type: klasa miejsca (np. pierwsza klasa, druga klasa).
    """
    TRAIN_CLASS_CHOICES = (
        ('first_class', 'Pierwsza klasa'),
        ('second_class', 'Druga klasa'),
    )

    train = models.ForeignKey(Train, on_delete=models.CASCADE)
    number = models.CharField(max_length=10, blank=False, null=False)
    class_type = models.CharField(max_length=20, choices=TRAIN_CLASS_CHOICES, default='second_class')

    def __str__(self):
        return f"Miejsce {self.number} - {self.train} ({self.get_class_type_display()})"


class Ticket(models.Model):
    """
    Model reprezentujący bilet pasażera na pociąg.

    Pola:
    - passenger: pasażer, do którego przypisany jest bilet.
    - seat: miejsce, na które nabyto bilet.
    - valid_date: data ważności biletu.
    - price: cena biletu.
    - status: status biletu (dostępny, zarezerwowany, potwierdzony).
    """
    STATUS_CHOICES = (
        ('available', 'Dostępny'),
        ('reserved', 'Zarezerwowany'),
        ('confirmed', 'Potwierdzony'),
    )

    passenger = models.ForeignKey(Passenger, on_delete=models.CASCADE)
    seat = models.ForeignKey(Seat, on_delete=models.CASCADE)
    valid_date = models.DateField()
    price = models.DecimalField(max_digits=7, decimal_places=2)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='available')

    def __str__(self):
        return f"Bilet {self.id} - {self.passenger} - {self.seat} - {self.valid_date} ({self.get_status_display()})"
