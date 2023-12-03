import os
import sys

def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bilety_kolejowe_projekt_pociagi.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()

    from Bilety_i_pociagi import models
    from django.utils import timezone

    # how database looks like and what fields it has
    # route: name (Kraków-Warszawa)
    # train_route: train, routes (Kraków-Warszawa) - many to many
    # train: train_id, travel_time in format 03:00:00, train_type, routes
    # schedule: train, departure_city, departure_time, arrival_city, arrival_time
    # passenger: first_name, last_name
    # seat: train, number, class_type
    # ticket: passenger, seat, valid_date, price, status

    # cities: Kraków, Warszawa, Gdańsk, Wrocław, Poznań, Szczecin

    def create_data():
        # all possibilities of routes between cities 
        # Kraków-Warszawa is different than Warszawa-Kraków
        models.Route.objects.get_or_create(name="Kraków-Warszawa")
        models.Route.objects.get_or_create(name="Kraków-Gdańsk")
        models.Route.objects.get_or_create(name="Kraków-Wrocław")
        models.Route.objects.get_or_create(name="Kraków-Poznań")
        models.Route.objects.get_or_create(name="Kraków-Szczecin")

        models.Route.objects.get_or_create(name="Warszawa-Kraków")
        models.Route.objects.get_or_create(name="Warszawa-Gdańsk")
        models.Route.objects.get_or_create(name="Warszawa-Wrocław")
        models.Route.objects.get_or_create(name="Warszawa-Poznań")
        models.Route.objects.get_or_create(name="Warszawa-Szczecin")

        models.Route.objects.get_or_create(name="Gdańsk-Kraków")
        models.Route.objects.get_or_create(name="Gdańsk-Warszawa")
        models.Route.objects.get_or_create(name="Gdańsk-Wrocław")
        models.Route.objects.get_or_create(name="Gdańsk-Poznań")
        models.Route.objects.get_or_create(name="Gdańsk-Szczecin")

        models.Route.objects.get_or_create(name="Wrocław-Kraków")
        models.Route.objects.get_or_create(name="Wrocław-Warszawa")
        models.Route.objects.get_or_create(name="Wrocław-Gdańsk")
        models.Route.objects.get_or_create(name="Wrocław-Poznań")
        models.Route.objects.get_or_create(name="Wrocław-Szczecin")

        models.Route.objects.get_or_create(name="Poznań-Kraków")
        models.Route.objects.get_or_create(name="Poznań-Warszawa")
        models.Route.objects.get_or_create(name="Poznań-Gdańsk")
        models.Route.objects.get_or_create(name="Poznań-Wrocław")
        models.Route.objects.get_or_create(name="Poznań-Szczecin")

        models.Route.objects.get_or_create(name="Szczecin-Kraków")
        models.Route.objects.get_or_create(name="Szczecin-Warszawa")
        models.Route.objects.get_or_create(name="Szczecin-Gdańsk")
        models.Route.objects.get_or_create(name="Szczecin-Wrocław")
        models.Route.objects.get_or_create(name="Szczecin-Poznań")


        # train_id: FT-(EXP/REG)0<NUMBER> (EXP - express, REG - regular) EXP 1-10, REG 1-27
        # travel_time is in format 03:00:00 and different for each train
        # train_type: express, regular (exp, reg)
        models.Train.objects.get_or_create(train_id="FT-EXP001", travel_time="03:00:00",
                                            train_type="exp")  # kraków-warszawa
        models.Train.objects.get_or_create(train_id="FT-EXP002", travel_time="03:00:00",
                                            train_type="exp")  # kraków-warszawa
        models.Train.objects.get_or_create(train_id="FT-EXP003", travel_time="01:40:00",
                                            train_type="exp")  # kraków-wrocław
        models.Train.objects.get_or_create(train_id="FT-EXP004", travel_time="03:30:00",
                                            train_type="exp")  # warszawa-gdańsk
        models.Train.objects.get_or_create(train_id="FT-EXP005", travel_time="03:30:00",
                                            train_type="exp")  # warszawa-gdańsk
        models.Train.objects.get_or_create(train_id="FT-EXP006", travel_time="03:30:00",
                                            train_type="exp")  # warszawa-wrocław
        models.Train.objects.get_or_create(train_id="FT-EXP007", travel_time="03:30:00",
                                            train_type="exp")  # warszawa-wrocław
        models.Train.objects.get_or_create(train_id="FT-EXP008", travel_time="01:40:00",
                                            train_type="exp")  # warszawa-poznań
        models.Train.objects.get_or_create(train_id="FT-EXP009", travel_time="04:00:00",
                                            train_type="exp")  # wrocław-szczecin
        models.Train.objects.get_or_create(train_id="FT-EXP010", travel_time="04:00:00",
                                            train_type="exp")  # wrocław-szczecin

        models.Train.objects.get_or_create(train_id="FT-REG001", travel_time="04:30:00",
                                            train_type="reg")  # kraków-warszawa
        models.Train.objects.get_or_create(train_id="FT-REG002", travel_time="04:30:00",
                                            train_type="reg")  # kraków-warszawa
        models.Train.objects.get_or_create(train_id="FT-REG003", travel_time="08:00:00",
                                            train_type="reg")  # kraków-gdańsk
        models.Train.objects.get_or_create(train_id="FT-REG004", travel_time="08:00:00",
                                            train_type="reg")  # kraków-gdańsk
        models.Train.objects.get_or_create(train_id="FT-REG005", travel_time="03:00:00",
                                            train_type="reg")  # kraków-wrocław
        models.Train.objects.get_or_create(train_id="FT-REG006", travel_time="05:00:00",
                                            train_type="reg")  # kraków-poznań
        models.Train.objects.get_or_create(train_id="FT-REG007", travel_time="05:00:00",
                                            train_type="reg")  # kraków-poznań
        models.Train.objects.get_or_create(train_id="FT-REG008", travel_time="09:30:00",
                                            train_type="reg")  # kraków-szczecin
        models.Train.objects.get_or_create(train_id="FT-REG009", travel_time="09:30:00",
                                            train_type="reg")  # kraków-szczecin
        models.Train.objects.get_or_create(train_id="FT-REG010", travel_time="04:15:00",
                                            train_type="reg")  # warszawa-gdańsk
        models.Train.objects.get_or_create(train_id="FT-REG011", travel_time="04:15:00",
                                            train_type="reg")  # warszawa-gdańsk
        models.Train.objects.get_or_create(train_id="FT-REG012", travel_time="05:00:00",
                                            train_type="reg")  # warszawa-wrocław
        models.Train.objects.get_or_create(train_id="FT-REG013", travel_time="05:00:00",
                                            train_type="reg")  # warszawa-wrocław
        models.Train.objects.get_or_create(train_id="FT-REG014", travel_time="02:30:00",
                                            train_type="reg")  # warszawa-poznań
        models.Train.objects.get_or_create(train_id="FT-REG015", travel_time="06:00:00",
                                            train_type="reg")  # warszawa-szczecin
        models.Train.objects.get_or_create(train_id="FT-REG016", travel_time="06:00:00",
                                            train_type="reg")  # warszawa-szczecin
        models.Train.objects.get_or_create(train_id="FT-REG017", travel_time="06:00:00",
                                            train_type="reg")  # gdańsk-wrocław
        models.Train.objects.get_or_create(train_id="FT-REG018", travel_time="06:00:00",
                                            train_type="reg")  # gdańsk-wrocław
        models.Train.objects.get_or_create(train_id="FT-REG019", travel_time="05:00:00",
                                            train_type="reg")  # gdańsk-poznań
        models.Train.objects.get_or_create(train_id="FT-REG020", travel_time="05:00:00",
                                            train_type="reg")  # gdańsk-poznań
        models.Train.objects.get_or_create(train_id="FT-REG021", travel_time="05:30:00",
                                            train_type="reg")  # gdańsk-szczecin
        models.Train.objects.get_or_create(train_id="FT-REG022", travel_time="05:30:00",
                                            train_type="reg")  # gdańsk-szczecin
        models.Train.objects.get_or_create(train_id="FT-REG023", travel_time="01:40:00",
                                            train_type="reg")  # wrocław-poznań
        models.Train.objects.get_or_create(train_id="FT-REG024", travel_time="06:00:00",
                                            train_type="reg")  # wrocław-szczecin
        models.Train.objects.get_or_create(train_id="FT-REG025", travel_time="06:00:00",
                                            train_type="reg")  # wrocław-szczecin
        models.Train.objects.get_or_create(train_id="FT-REG026", travel_time="03:00:00",
                                            train_type="reg")  # poznań-szczecin
        models.Train.objects.get_or_create(train_id="FT-REG027", travel_time="03:00:00",
                                            train_type="reg")  # poznań-szczecin


        # train_route: train, route (Kraków-Warszawa) - many to many
        models.TrainRoute.objects.get_or_create(train=models.Train.objects.get(train_id="FT-EXP001"),
                                                route=models.Route.objects.get(name="Kraków-Warszawa"))
        models.TrainRoute.objects.get_or_create(train=models.Train.objects.get(train_id="FT-EXP001"),
                                                route=models.Route.objects.get(name="Warszawa-Kraków"))
        models.TrainRoute.objects.get_or_create(train=models.Train.objects.get(train_id="FT-EXP002"),
                                                route=models.Route.objects.get(name="Kraków-Warszawa"))
        models.TrainRoute.objects.get_or_create(train=models.Train.objects.get(train_id="FT-EXP002"),
                                                route=models.Route.objects.get(name="Warszawa-Kraków"))

        models.TrainRoute.objects.get_or_create(train=models.Train.objects.get(train_id="FT-EXP003"),
                                                route=models.Route.objects.get(name="Kraków-Wrocław"))
        models.TrainRoute.objects.get_or_create(train=models.Train.objects.get(train_id="FT-EXP003"),
                                                route=models.Route.objects.get(name="Wrocław-Kraków"))

        models.TrainRoute.objects.get_or_create(train=models.Train.objects.get(train_id="FT-EXP004"),
                                                route=models.Route.objects.get(name="Warszawa-Gdańsk"))
        models.TrainRoute.objects.get_or_create(train=models.Train.objects.get(train_id="FT-EXP004"),
                                                route=models.Route.objects.get(name="Gdańsk-Warszawa"))
        models.TrainRoute.objects.get_or_create(train=models.Train.objects.get(train_id="FT-EXP005"),
                                                route=models.Route.objects.get(name="Warszawa-Gdańsk"))
        models.TrainRoute.objects.get_or_create(train=models.Train.objects.get(train_id="FT-EXP005"),
                                                route=models.Route.objects.get(name="Gdańsk-Warszawa"))

        models.TrainRoute.objects.get_or_create(train=models.Train.objects.get(train_id="FT-EXP006"),
                                                route=models.Route.objects.get(name="Warszawa-Wrocław"))
        models.TrainRoute.objects.get_or_create(train=models.Train.objects.get(train_id="FT-EXP006"),
                                                route=models.Route.objects.get(name="Wrocław-Warszawa"))
        models.TrainRoute.objects.get_or_create(train=models.Train.objects.get(train_id="FT-EXP007"),
                                                route=models.Route.objects.get(name="Warszawa-Wrocław"))
        models.TrainRoute.objects.get_or_create(train=models.Train.objects.get(train_id="FT-EXP007"),
                                                route=models.Route.objects.get(name="Wrocław-Warszawa"))

        models.TrainRoute.objects.get_or_create(train=models.Train.objects.get(train_id="FT-EXP008"),
                                                route=models.Route.objects.get(name="Warszawa-Poznań"))
        models.TrainRoute.objects.get_or_create(train=models.Train.objects.get(train_id="FT-EXP008"),
                                                route=models.Route.objects.get(name="Poznań-Warszawa"))

        models.TrainRoute.objects.get_or_create(train=models.Train.objects.get(train_id="FT-EXP009"),
                                                route=models.Route.objects.get(name="Wrocław-Szczecin"))
        models.TrainRoute.objects.get_or_create(train=models.Train.objects.get(train_id="FT-EXP009"),
                                                route=models.Route.objects.get(name="Szczecin-Wrocław"))
        models.TrainRoute.objects.get_or_create(train=models.Train.objects.get(train_id="FT-EXP010"),
                                                route=models.Route.objects.get(name="Wrocław-Szczecin"))
        models.TrainRoute.objects.get_or_create(train=models.Train.objects.get(train_id="FT-EXP010"),
                                                route=models.Route.objects.get(name="Szczecin-Wrocław"))

        models.TrainRoute.objects.get_or_create(train=models.Train.objects.get(train_id="FT-REG001"),
                                                route=models.Route.objects.get(name="Kraków-Warszawa"))
        models.TrainRoute.objects.get_or_create(train=models.Train.objects.get(train_id="FT-REG001"),
                                                route=models.Route.objects.get(name="Warszawa-Kraków"))
        models.TrainRoute.objects.get_or_create(train=models.Train.objects.get(train_id="FT-REG002"),
                                                route=models.Route.objects.get(name="Kraków-Warszawa"))
        models.TrainRoute.objects.get_or_create(train=models.Train.objects.get(train_id="FT-REG002"),
                                                route=models.Route.objects.get(name="Warszawa-Kraków"))

        models.TrainRoute.objects.get_or_create(train=models.Train.objects.get(train_id="FT-REG003"),
                                                route=models.Route.objects.get(name="Kraków-Gdańsk"))
        models.TrainRoute.objects.get_or_create(train=models.Train.objects.get(train_id="FT-REG003"),
                                                route=models.Route.objects.get(name="Gdańsk-Kraków"))
        models.TrainRoute.objects.get_or_create(train=models.Train.objects.get(train_id="FT-REG004"),
                                                route=models.Route.objects.get(name="Kraków-Gdańsk"))
        models.TrainRoute.objects.get_or_create(train=models.Train.objects.get(train_id="FT-REG004"),
                                                route=models.Route.objects.get(name="Gdańsk-Kraków"))

        models.TrainRoute.objects.get_or_create(train=models.Train.objects.get(train_id="FT-REG005"),
                                                route=models.Route.objects.get(name="Kraków-Wrocław"))
        models.TrainRoute.objects.get_or_create(train=models.Train.objects.get(train_id="FT-REG005"),
                                                route=models.Route.objects.get(name="Wrocław-Kraków"))

        models.TrainRoute.objects.get_or_create(train=models.Train.objects.get(train_id="FT-REG006"),
                                                route=models.Route.objects.get(name="Kraków-Poznań"))
        models.TrainRoute.objects.get_or_create(train=models.Train.objects.get(train_id="FT-REG006"),
                                                route=models.Route.objects.get(name="Poznań-Kraków"))
        models.TrainRoute.objects.get_or_create(train=models.Train.objects.get(train_id="FT-REG007"),
                                                route=models.Route.objects.get(name="Kraków-Poznań"))
        models.TrainRoute.objects.get_or_create(train=models.Train.objects.get(train_id="FT-REG007"),
                                                route=models.Route.objects.get(name="Poznań-Kraków"))

        models.TrainRoute.objects.get_or_create(train=models.Train.objects.get(train_id="FT-REG008"),
                                                route=models.Route.objects.get(name="Kraków-Szczecin"))
        models.TrainRoute.objects.get_or_create(train=models.Train.objects.get(train_id="FT-REG008"),
                                                route=models.Route.objects.get(name="Szczecin-Kraków"))
        models.TrainRoute.objects.get_or_create(train=models.Train.objects.get(train_id="FT-REG009"),
                                                route=models.Route.objects.get(name="Kraków-Szczecin"))
        models.TrainRoute.objects.get_or_create(train=models.Train.objects.get(train_id="FT-REG009"),
                                                route=models.Route.objects.get(name="Szczecin-Kraków"))

        models.TrainRoute.objects.get_or_create(train=models.Train.objects.get(train_id="FT-REG010"),
                                                route=models.Route.objects.get(name="Warszawa-Gdańsk"))
        models.TrainRoute.objects.get_or_create(train=models.Train.objects.get(train_id="FT-REG010"),
                                                route=models.Route.objects.get(name="Gdańsk-Warszawa"))
        models.TrainRoute.objects.get_or_create(train=models.Train.objects.get(train_id="FT-REG011"),
                                                route=models.Route.objects.get(name="Warszawa-Gdańsk"))
        models.TrainRoute.objects.get_or_create(train=models.Train.objects.get(train_id="FT-REG011"),
                                                route=models.Route.objects.get(name="Gdańsk-Warszawa"))

        models.TrainRoute.objects.get_or_create(train=models.Train.objects.get(train_id="FT-REG012"),
                                                route=models.Route.objects.get(name="Warszawa-Wrocław"))
        models.TrainRoute.objects.get_or_create(train=models.Train.objects.get(train_id="FT-REG012"),
                                                route=models.Route.objects.get(name="Wrocław-Warszawa"))
        models.TrainRoute.objects.get_or_create(train=models.Train.objects.get(train_id="FT-REG013"),
                                                route=models.Route.objects.get(name="Warszawa-Wrocław"))
        models.TrainRoute.objects.get_or_create(train=models.Train.objects.get(train_id="FT-REG013"),
                                                route=models.Route.objects.get(name="Wrocław-Warszawa"))

        models.TrainRoute.objects.get_or_create(train=models.Train.objects.get(train_id="FT-REG014"),
                                                route=models.Route.objects.get(name="Warszawa-Poznań"))
        models.TrainRoute.objects.get_or_create(train=models.Train.objects.get(train_id="FT-REG014"),
                                                route=models.Route.objects.get(name="Poznań-Warszawa"))

        models.TrainRoute.objects.get_or_create(train=models.Train.objects.get(train_id="FT-REG015"),
                                                route=models.Route.objects.get(name="Warszawa-Szczecin"))
        models.TrainRoute.objects.get_or_create(train=models.Train.objects.get(train_id="FT-REG015"),
                                                route=models.Route.objects.get(name="Szczecin-Warszawa"))
        models.TrainRoute.objects.get_or_create(train=models.Train.objects.get(train_id="FT-REG016"),
                                                route=models.Route.objects.get(name="Warszawa-Szczecin"))
        models.TrainRoute.objects.get_or_create(train=models.Train.objects.get(train_id="FT-REG016"),
                                                route=models.Route.objects.get(name="Szczecin-Warszawa"))

        models.TrainRoute.objects.get_or_create(train=models.Train.objects.get(train_id="FT-REG017"),
                                                route=models.Route.objects.get(name="Gdańsk-Wrocław"))
        models.TrainRoute.objects.get_or_create(train=models.Train.objects.get(train_id="FT-REG017"),
                                                route=models.Route.objects.get(name="Wrocław-Gdańsk"))
        models.TrainRoute.objects.get_or_create(train=models.Train.objects.get(train_id="FT-REG018"),
                                                route=models.Route.objects.get(name="Gdańsk-Wrocław"))
        models.TrainRoute.objects.get_or_create(train=models.Train.objects.get(train_id="FT-REG018"),
                                                route=models.Route.objects.get(name="Wrocław-Gdańsk"))

        models.TrainRoute.objects.get_or_create(train=models.Train.objects.get(train_id="FT-REG019"),
                                                route=models.Route.objects.get(name="Gdańsk-Poznań"))
        models.TrainRoute.objects.get_or_create(train=models.Train.objects.get(train_id="FT-REG019"),
                                                route=models.Route.objects.get(name="Poznań-Gdańsk"))
        models.TrainRoute.objects.get_or_create(train=models.Train.objects.get(train_id="FT-REG020"),
                                                route=models.Route.objects.get(name="Gdańsk-Poznań"))
        models.TrainRoute.objects.get_or_create(train=models.Train.objects.get(train_id="FT-REG020"),
                                                route=models.Route.objects.get(name="Poznań-Gdańsk"))

        models.TrainRoute.objects.get_or_create(train=models.Train.objects.get(train_id="FT-REG021"),
                                                route=models.Route.objects.get(name="Gdańsk-Szczecin"))
        models.TrainRoute.objects.get_or_create(train=models.Train.objects.get(train_id="FT-REG021"),
                                                route=models.Route.objects.get(name="Szczecin-Gdańsk"))
        models.TrainRoute.objects.get_or_create(train=models.Train.objects.get(train_id="FT-REG022"),
                                                route=models.Route.objects.get(name="Gdańsk-Szczecin"))
        models.TrainRoute.objects.get_or_create(train=models.Train.objects.get(train_id="FT-REG022"),
                                                route=models.Route.objects.get(name="Szczecin-Gdańsk"))

        models.TrainRoute.objects.get_or_create(train=models.Train.objects.get(train_id="FT-REG023"),
                                                route=models.Route.objects.get(name="Wrocław-Poznań"))
        models.TrainRoute.objects.get_or_create(train=models.Train.objects.get(train_id="FT-REG023"),
                                                route=models.Route.objects.get(name="Poznań-Wrocław"))

        models.TrainRoute.objects.get_or_create(train=models.Train.objects.get(train_id="FT-REG024"),
                                                route=models.Route.objects.get(name="Wrocław-Szczecin"))
        models.TrainRoute.objects.get_or_create(train=models.Train.objects.get(train_id="FT-REG024"),
                                                route=models.Route.objects.get(name="Szczecin-Wrocław"))
        models.TrainRoute.objects.get_or_create(train=models.Train.objects.get(train_id="FT-REG025"),
                                                route=models.Route.objects.get(name="Wrocław-Szczecin"))
        models.TrainRoute.objects.get_or_create(train=models.Train.objects.get(train_id="FT-REG025"),
                                                route=models.Route.objects.get(name="Szczecin-Wrocław"))

        models.TrainRoute.objects.get_or_create(train=models.Train.objects.get(train_id="FT-REG026"),
                                                route=models.Route.objects.get(name="Poznań-Szczecin"))
        models.TrainRoute.objects.get_or_create(train=models.Train.objects.get(train_id="FT-REG026"),
                                                route=models.Route.objects.get(name="Szczecin-Poznań"))
        models.TrainRoute.objects.get_or_create(train=models.Train.objects.get(train_id="FT-REG027"),
                                                route=models.Route.objects.get(name="Poznań-Szczecin"))
        models.TrainRoute.objects.get_or_create(train=models.Train.objects.get(train_id="FT-REG027"),
                                                route=models.Route.objects.get(name="Szczecin-Poznań"))


        # schedule: train, departure_city, departure_time, arrival_city, arrival_time

        def calculate_arrival_time(departure_time_str, travel_time_str):
                departure_time = timezone.datetime.strptime(departure_time_str, "%H:%M:%S").time()
                hours, minutes, seconds = map(int, travel_time_str.split(':'))
                travel_time = timezone.timedelta(hours=hours, minutes=minutes, seconds=seconds)
                arrival_time = (timezone.datetime.combine(timezone.now(), departure_time) + travel_time).time()
                return arrival_time

        def create_schedule(train_id, departure_city, arrival_city, departure_time_str, travel_time_str):
            train = models.Train.objects.get(train_id=train_id)
            departure_time = timezone.datetime.strptime(departure_time_str, "%H:%M:%S").time()
            arrival_time = calculate_arrival_time(departure_time_str, travel_time_str)

            models.Schedule.objects.get_or_create(  train=train,
                                                    departure_city=departure_city,
                                                    arrival_city=arrival_city,
                                                    departure_time=departure_time,
                                                    arrival_time=arrival_time
                                                    )

        ### express trains ###

        # Kraków-Warszawa and Warszawa-Kraków (only express trains)
        trains_ids = ["FT-EXP001", "FT-EXP002"]
        departures = ["08:00:00", "12:00:00", "16:00:00", "20:00:00"]
        stations = ["Kraków", "Warszawa"]

        for idx, train_id in enumerate(trains_ids):
            start_station_index = idx % 2

            for departure_idx, departure in enumerate(departures):
                departure_city = stations[(start_station_index + departure_idx) % 2]
                arrival_city = stations[(start_station_index + departure_idx + 1) % 2]

                create_schedule(train_id, departure_city, arrival_city, departure, models.Train.objects.get(train_id=train_id).travel_time)

        # Kraków-Wrocław and Wrocław-Kraków (only express trains)
        train_id = "FT-EXP003"
        departures = ["07:00:00", "13:40:00", "20:20:00", "02:00:00"]
        stations = ["Kraków", "Wrocław"]

        for idx, departure in enumerate(departures):
            departure_city = stations[idx % 2]
            arrival_city = stations[(idx + 1) % 2]

            create_schedule(train_id, departure_city, arrival_city, departure, models.Train.objects.get(train_id=train_id).travel_time)

        # Warszawa-Gdańsk and Gdańsk-Warszawa (only express trains)
        trains_ids = ["FT-EXP004", "FT-EXP005"]
        departures = ["06:00:00", "10:00:00", "14:00:00", "18:00:00"]
        stations = ["Warszawa", "Gdańsk"]

        for idx, train_id in enumerate(trains_ids):
            start_station_index = idx % 2

            for departure_idx, departure in enumerate(departures):
                departure_city = stations[(start_station_index + departure_idx) % 2]
                arrival_city = stations[(start_station_index + departure_idx + 1) % 2]

                create_schedule(train_id, departure_city, arrival_city, departure, models.Train.objects.get(train_id=train_id).travel_time)

        # Warszawa-Wrocław and Wrocław-Warszawa (only express trains)
        trains_ids = ["FT-EXP006", "FT-EXP007"]
        departures = ["07:30:00", "11:30:00", "15:30:00", "19:30:00"]
        stations = ["Warszawa", "Wrocław"]

        for idx, train_id in enumerate(trains_ids):
            start_station_index = idx % 2

            for departure_idx, departure in enumerate(departures):
                departure_city = stations[(start_station_index + departure_idx) % 2]
                arrival_city = stations[(start_station_index + departure_idx + 1) % 2]

                create_schedule(train_id, departure_city, arrival_city, departure, models.Train.objects.get(train_id=train_id).travel_time)

        # Warszawa-Poznań and Poznań-Warszawa (only express trains)
        train_id = "FT-EXP008"
        departures = ["10:00:00", "18:00:00"]
        stations = ["Warszawa", "Poznań"]

        for idx, departure in enumerate(departures):
            departure_city = stations[idx % 2]
            arrival_city = stations[(idx + 1) % 2]

            create_schedule(train_id, departure_city, arrival_city, departure, models.Train.objects.get(train_id=train_id).travel_time)

        # Wrocław-Szczecin and Szczecin-Wrocław (only express trains)
        trains_ids = ["FT-EXP009", "FT-EXP010"]
        departures = ["09:12:00", "17:12:00"]
        stations = ["Wrocław", "Szczecin"]

        for idx, train_id in enumerate(trains_ids):
            start_station_index = idx % 2

            for departure_idx, departure in enumerate(departures):
                departure_city = stations[(start_station_index + departure_idx) % 2]
                arrival_city = stations[(start_station_index + departure_idx + 1) % 2]

                create_schedule(train_id, departure_city, arrival_city, departure, models.Train.objects.get(train_id=train_id).travel_time)

        ### regular trains ###

        # Kraków-Warszawa and Warszawa-Kraków (only regular trains)
        trains_ids = ["FT-REG001", "FT-REG002"]
        departures = ["07:00:00", "12:30:00", "18:00:00", "00:00:00"]
        stations = ["Kraków", "Warszawa"]

        for idx, train_id in enumerate(trains_ids):
            start_station_index = idx % 2

            for departure_idx, departure in enumerate(departures):
                departure_city = stations[(start_station_index + departure_idx) % 2]
                arrival_city = stations[(start_station_index + departure_idx + 1) % 2]

                create_schedule(train_id, departure_city, arrival_city, departure, models.Train.objects.get(train_id=train_id).travel_time)

        # Kraków-Gdańsk and Gdańsk-Kraków (only regular trains)
        trains_ids = ["FT-REG003", "FT-REG004"]
        departures = ["10:00:00", "22:00:00"]
        stations = ["Kraków", "Gdańsk"]

        for idx, train_id in enumerate(trains_ids):
            start_station_index = idx % 2

            for departure_idx, departure in enumerate(departures):
                departure_city = stations[(start_station_index + departure_idx) % 2]
                arrival_city = stations[(start_station_index + departure_idx + 1) % 2]

                create_schedule(train_id, departure_city, arrival_city, departure, models.Train.objects.get(train_id=train_id).travel_time)

        # Kraków-Wrocław and Wrocław-Kraków (only regular trains)
        train_id = "FT-REG005"
        departures = ["06:00:00", "18:00:00"]
        stations = ["Kraków", "Wrocław"]

        for idx, departure in enumerate(departures):
            departure_city = stations[idx % 2]
            arrival_city = stations[(idx + 1) % 2]

            create_schedule(train_id, departure_city, arrival_city, departure, models.Train.objects.get(train_id=train_id).travel_time)

        # Kraków-Poznań and Poznań-Kraków (only regular trains)
        trains_ids = ["FT-REG006", "FT-REG007"]
        departures = ["06:05:00", "11:45:00", "18:05:00", "00:15:00"]
        stations = ["Kraków", "Poznań"]

        for idx, train_id in enumerate(trains_ids):
            start_station_index = idx % 2

            for departure_idx, departure in enumerate(departures):
                departure_city = stations[(start_station_index + departure_idx) % 2]
                arrival_city = stations[(start_station_index + departure_idx + 1) % 2]

                create_schedule(train_id, departure_city, arrival_city, departure, models.Train.objects.get(train_id=train_id).travel_time)

        # Kraków-Szczecin and Szczecin-Kraków (only regular trains)
        trains_ids = ["FT-REG008", "FT-REG009"]
        departures = ["08:30:00", "20:30:00"]
        stations = ["Kraków", "Szczecin"]

        for idx, train_id in enumerate(trains_ids):
            start_station_index = idx % 2

            for departure_idx, departure in enumerate(departures):
                departure_city = stations[(start_station_index + departure_idx) % 2]
                arrival_city = stations[(start_station_index + departure_idx + 1) % 2]

                create_schedule(train_id, departure_city, arrival_city, departure, models.Train.objects.get(train_id=train_id).travel_time)

        # Warszawa-Gdańsk and Gdańsk-Warszawa (only regular trains)
        trains_ids = ["FT-REG010", "FT-REG011"]
        departures = ["06:15:00", "11:00:00", "15:45:00", "20:30:00"]
        stations = ["Warszawa", "Gdańsk"]

        for idx, train_id in enumerate(trains_ids):
            start_station_index = idx % 2

            for departure_idx, departure in enumerate(departures):
                departure_city = stations[(start_station_index + departure_idx) % 2]
                arrival_city = stations[(start_station_index + departure_idx + 1) % 2]

                create_schedule(train_id, departure_city, arrival_city, departure, models.Train.objects.get(train_id=train_id).travel_time)

        # Warszawa-Wrocław and Wrocław-Warszawa (only regular trains)
        trains_ids = ["FT-REG012", "FT-REG013"]
        departures = ["08:08:00", "13:38:00", "19:08:00", "00:38:00"]
        stations = ["Warszawa", "Wrocław"]

        for idx, train_id in enumerate(trains_ids):
            start_station_index = idx % 2

            for departure_idx, departure in enumerate(departures):
                departure_city = stations[(start_station_index + departure_idx) % 2]
                arrival_city = stations[(start_station_index + departure_idx + 1) % 2]

                create_schedule(train_id, departure_city, arrival_city, departure, models.Train.objects.get(train_id=train_id).travel_time)

        # Warszawa-Poznań and Poznań-Warszawa (only regular trains)
        train_id = "FT-REG014"
        departures = ["07:36:00", "21:26:00"]
        stations = ["Warszawa", "Poznań"]

        for idx, departure in enumerate(departures):
            departure_city = stations[idx % 2]
            arrival_city = stations[(idx + 1) % 2]

            create_schedule(train_id, departure_city, arrival_city, departure, models.Train.objects.get(train_id=train_id).travel_time)

        # Warszawa-Szczecin and Szczecin-Warszawa (only regular trains)
        trains_ids = ["FT-REG015", "FT-REG016"]
        departures = ["11:15:00", "18:45:00"]
        stations = ["Warszawa", "Szczecin"]

        for idx, train_id in enumerate(trains_ids):
            start_station_index = idx % 2

            for departure_idx, departure in enumerate(departures):
                departure_city = stations[(start_station_index + departure_idx) % 2]
                arrival_city = stations[(start_station_index + departure_idx + 1) % 2]

                create_schedule(train_id, departure_city, arrival_city, departure, models.Train.objects.get(train_id=train_id).travel_time)

        # Gdańsk-Wrocław and Wrocław-Gdańsk (only regular trains)
        trains_ids = ["FT-REG017", "FT-REG018"]
        departures = ["13:13:00", "21:13:00"]
        stations = ["Gdańsk", "Wrocław"]

        for idx, train_id in enumerate(trains_ids):
            start_station_index = idx % 2

            for departure_idx, departure in enumerate(departures):
                departure_city = stations[(start_station_index + departure_idx) % 2]
                arrival_city = stations[(start_station_index + departure_idx + 1) % 2]

                create_schedule(train_id, departure_city, arrival_city, departure, models.Train.objects.get(train_id=train_id).travel_time)

        # Gdańsk-Poznań and Poznań-Gdańsk (only regular trains)
        trains_ids = ["FT-REG019", "FT-REG020"]
        departures = ["06:20:00", "12:00:00", "18:20:00", "00:00:00"]
        stations = ["Gdańsk", "Poznań"]

        for idx, train_id in enumerate(trains_ids):
            start_station_index = idx % 2

            for departure_idx, departure in enumerate(departures):
                departure_city = stations[(start_station_index + departure_idx) % 2]
                arrival_city = stations[(start_station_index + departure_idx + 1) % 2]
                create_schedule(train_id, departure_city, arrival_city, departure, models.Train.objects.get(train_id=train_id).travel_time)

        # Gdańsk-Szczecin and Szczecin-Gdańsk (only regular trains)
        trains_ids = ["FT-REG021", "FT-REG022"]
        departures = ["07:07:00", "15:32:00"]
        stations = ["Gdańsk", "Szczecin"]

        for idx, train_id in enumerate(trains_ids):
            start_station_index = idx % 2

            for departure_idx, departure in enumerate(departures):
                departure_city = stations[(start_station_index + departure_idx) % 2]
                arrival_city = stations[(start_station_index + departure_idx + 1) % 2]
                create_schedule(train_id, departure_city, arrival_city, departure, models.Train.objects.get(train_id=train_id).travel_time)

        # Wrocław-Poznań and Poznań-Wrocław (only regular trains)
        train_id = "FT-REG023"
        departures = ["07:00:00", "13:00:00", "19:00:00", "01:00:00"]
        stations = ["Wrocław", "Poznań"]

        for idx, departure in enumerate(departures):
            departure_city = stations[idx % 2]
            arrival_city = stations[(idx + 1) % 2]

            create_schedule(train_id, departure_city, arrival_city, departure, models.Train.objects.get(train_id=train_id).travel_time)

        # Wrocław-Szczecin and Szczecin-Wrocław (only regular trains)
        trains_ids = ["FT-REG024", "FT-REG025"]
        departures = ["10:11:00", "22:11:00"]
        stations = ["Wrocław", "Szczecin"]

        for idx, train_id in enumerate(trains_ids):
            start_station_index = idx % 2

            for departure_idx, departure in enumerate(departures):
                departure_city = stations[(start_station_index + departure_idx) % 2]
                arrival_city = stations[(start_station_index + departure_idx + 1) % 2]
                create_schedule(train_id, departure_city, arrival_city, departure, models.Train.objects.get(train_id=train_id).travel_time)

        # Poznań-Szczecin and Szczecin-Poznań (only regular trains)
        trains_ids = ["FT-REG026", "FT-REG027"]
        departures = ["08:17:00", "14:37:00"]
        stations = ["Poznań", "Szczecin"]

        for idx, train_id in enumerate(trains_ids):
            start_station_index = idx % 2

            for departure_idx, departure in enumerate(departures):
                departure_city = stations[(start_station_index + departure_idx) % 2]
                arrival_city = stations[(start_station_index + departure_idx + 1) % 2]
                create_schedule(train_id, departure_city, arrival_city, departure, models.Train.objects.get(train_id=train_id).travel_time)


        # create passengers: (only one in case if no one is logged in)
        # passenger: first_name, last_name
        models.Passenger.objects.get_or_create(first_name="Mateusz", last_name="Walas")

        # seat: train, number, class_type
        # 1st class is Premium, 2nd class is Standard
        # in express trains there are 60% of seats in Premium class and 40% of seats in Standard class
        # in regular trains there are 50% of seats in Premium class and 50% of seats in Standard class
        # in database there are 10 seats in each train
        # the names of seats are in format: [class-id (P or S)][seat_number in format 01-10]
        # for example: P01, S10

        express_trains_ids = [f"FT-EXP{i:03d}" for i in range(1, 11)]
        regular_trains_ids = [f"FT-REG{i:03d}" for i in range(1, 28)]
        total_seats = 10 # number of seats in each train

        def create_seats_for_train(train_id, premium_seats, standard_seats):
            train = models.Train.objects.get(train_id=train_id)

            for seat_number in range(1, premium_seats + 1):
                seat_id = f"P{seat_number:02d}"
                models.Seat.objects.get_or_create(train=train, number=seat_id, class_type='first_class')

            for seat_number in range(1, standard_seats + 1):
                seat_id = f"S{seat_number:02d}"
                models.Seat.objects.get_or_create(train=train, number=seat_id, class_type='second_class')

        for train_id in express_trains_ids:
            create_seats_for_train(train_id, int(total_seats * 0.6), total_seats - int(total_seats * 0.6))

        for train_id in regular_trains_ids:
            create_seats_for_train(train_id, total_seats // 2, total_seats // 2)

        # create price for tickets on each route
        # price: train, route, price
        # price on Kraków-Warszawa and Warszawa-Kraków is the same, in other cases it is the same too
        prices = {
            'Kraków-Warszawa': {'exp': 180.00, 'reg': 75.00},
            'Kraków-Gdańsk': {'reg': 250.00},
            'Kraków-Wrocław': {'exp': 220.00, 'reg': 160.00},
            'Kraków-Poznań': {'reg': 220.00},
            'Kraków-Szczecin': {'reg': 330.00},
            'Warszawa-Gdańsk': {'exp': 210.00, 'reg': 130.00},
            'Warszawa-Wrocław': {'exp': 200.00, 'reg': 150.00},
            'Warszawa-Poznań': {'exp': 185.00, 'reg': 140.00},
            'Warszawa-Szczecin': {'reg': 250.00},
            'Wrocław-Gdańsk': {'reg': 290.00},
            'Wrocław-Poznań': {'reg': 90.00},
            'Wrocław-Szczecin': {'exp': 310.00, 'reg': 250.00},
            'Poznań-Gdańsk': {'reg': 210.00},
            'Poznań-Szczecin': {'reg': 150.00},
            'Gdańsk-Szczecin': {'reg': 230.00}
        }

        def create_ticket_price(route_name, route_prices):
            try:
                route = models.Route.objects.get(name=route_name)
                for train_route in models.TrainRoute.objects.filter(route=route):
                    train = train_route.train
                    if train.train_type in route_prices:
                        price = route_prices[train.train_type]
                        models.TicketPrice.objects.get_or_create(
                            train=train,
                            route=route,
                            defaults={'price': price}
                        )
            except models.Route.DoesNotExist:
                print(f"Route {route_name} does not exist")

        for route_name, route_prices in prices.items():
            create_ticket_price(route_name, route_prices)
            
            reverse_route_name = '-'.join(route_name.split('-')[::-1])
            if reverse_route_name not in prices:
                create_ticket_price(reverse_route_name, route_prices)

        # no tickets are created at the beginning of the database creation
        # if in database there are no tickets, it is meant that no one bought any tickets yet

    create_data()
