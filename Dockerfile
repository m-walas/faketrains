FROM python:3.11

RUN pip install --upgrade pip
RUN apt-get update && apt-get install -y build-essential libssl-dev

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV RUNNING_IN_DOCKER=true

WORKDIR /app
COPY requirements.txt /app/

RUN pip install --no-cache-dir -r requirements.txt

COPY . /app/

RUN python manage.py migrate
RUN python manage.py collectstatic --noinput

EXPOSE 5000
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "bilety_kolejowe_projekt_pociagi.wsgi:application"]
