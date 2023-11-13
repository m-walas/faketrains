# Wybierz obraz bazowy zgodny z Twoim projektem Django (np. Python)
FROM python:3.8
LABEL authors="Mateusz"

# Ustal katalog roboczy w kontenerze
WORKDIR /app

# Zainstaluj zależności backendu Django
COPY requirements.txt /app/
RUN pip install -r requirements.txt

# Skopiuj kod źródłowy Django do kontenera
COPY . /app/

# Zbuduj aplikację Django
RUN python manage.py migrate

# Ustaw zmienne środowiskowe dla aplikacji Django
ENV DJANGO_SETTINGS_MODULE=bilety_kolejowe_projekt_pociagi.settings

# Uruchom serwer Django na porcie 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
