#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
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
        # create all possibilities of routes between cities Kraków-Warszawa is different than Warszawa-Kraków
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

        # create trains:
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

        # create train routes for each train:
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

        # create schedules for each train:
        # schedule: train, departure_city, departure_time, arrival_city, arrival_time
        models.Schedule.objects.get_or_create(train=models.Train.objects.get(train_id="FT-EXP001"),
                                              departure_city="Kraków", departure_time="08:00:00",
                                              arrival_city="Warszawa", arrival_time="11:00:00")
        models.Schedule.objects.get_or_create(train=models.Train.objects.get(train_id="FT-EXP002"),
                                              departure_city="Warszawa", departure_time="12:00:00",
                                              arrival_city="Kraków", arrival_time="15:00:00")
        # TODO TODO TODO TODO TODO TODO

        # create passengers: (only one in case if no one is logged in)
        # passenger: first_name, last_name
        models.Passenger.objects.get_or_create(first_name="Mateusz", last_name="Walas")

        # create seats for each train:
        # seat: train, number, class_type
        # in loop
        # TODO

        # create tickets for each passenger:
        # no tickets are created at the beginning of the database creation

        # print("Checked 30/30 routes.")
        # print("Checked 10/10 exp trains.")
        # print("Checked 27/27 reg trains.")
        # print("Data created successfully!")


    create_data()
