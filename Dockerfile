FROM python:3.9-alpine

ENV PYTHONUNBUFFERED 1


COPY . /app

WORKDIR /app

RUN pip3 install -r requirements.txt


RUN python manage.py makemigrations

RUN python manage.py migrate



CMD [ "python", "manage.py", "runserver", "0.0.0.0:8000" ]
