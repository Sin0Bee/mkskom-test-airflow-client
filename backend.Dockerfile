FROM python:3.11-alpine

COPY requirements.txt /temp/requirements.txt
COPY . /backend

WORKDIR /backend

EXPOSE 8000

RUN pip install -r /temp/requirements.txt
RUN adduser --disabled-password service-user

USER service-user