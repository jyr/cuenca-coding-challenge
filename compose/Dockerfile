FROM python:3.7-alpine

RUN apk update \
    && apk add --no-cache --virtual bash \
    && apk add gcc \
    && apk add musl-dev \
    && apk add postgresql-dev \
    && apk add linux-headers \
    && apk add libffi-dev \
    && apk add curl \
    && apk add vim

# install pypi packages
COPY requirements_dev.txt /requirements_dev.txt

RUN pip install --upgrade pip \
    && pip install -r requirements_dev.txt

WORKDIR /code/

USER 1000:1000
