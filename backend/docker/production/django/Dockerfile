FROM python:3.10.1-slim-buster

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

RUN apt-get update -y && apt-get install -y \
    software-properties-common \
    gettext \
    python3-software-properties \
    build-essential \
    python3-dev \
    postgresql-client

COPY ./backend /app/

RUN python -m pip install --upgrade pip
COPY ./backend/config/requirements /requirements
RUN pip install -r /requirements/production.txt

COPY ./backend/docker/production/django/start /start
RUN sed -i 's/\r$//g' /start
RUN chmod +x /start

WORKDIR /app

ENTRYPOINT ["/start"]
