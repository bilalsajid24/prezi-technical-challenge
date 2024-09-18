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

RUN python -m pip install --upgrade pip
COPY ./config/requirements /requirements
RUN pip install -r /requirements/local.txt

COPY ./docker/local/django/entrypoint /entrypoint
RUN sed -i 's/\r$//g' /entrypoint
RUN chmod +x /entrypoint

COPY ./docker/local/django/start /start
RUN sed -i 's/\r$//g' /start
RUN chmod +x /start

WORKDIR /app

ENTRYPOINT ["/entrypoint"]
