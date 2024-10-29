FROM python:3.12.2-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

RUN apt update -y && \
    apt install -y python3-dev \
    gcc \
    musl-dev \
    libpq-dev \
    nmap

COPY requirements.txt /app/

RUN pip install --upgrade pip \
 && pip install -r requirements.txt

COPY ./app /app/app/
COPY ./migrations /app/migrations/
COPY entrypoint.sh /app/entrypoint.sh
COPY config.py /app/config.py

RUN chmod +x /app/entrypoint.sh
