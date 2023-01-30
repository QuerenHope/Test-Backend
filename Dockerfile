FROM python:3.11

ENV PYTHONDONTWRITEBYTECODE 1

ENV PYTHONUNBUFFERED 1

WORKDIR /django_app

COPY . /django_app/

RUN pip install -U pip
RUN pip install -r requirements.txt