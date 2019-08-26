FROM python:3.7-alpine

RUN apk update \
    && apk add --no-cache --virtual bash \
    && apk add gcc \
    && apk add musl-dev \
    && apk add linux-headers \
    && apk add libffi-dev \
    && apk add curl \
    && apk add vim

# install pypi packages
#COPY requirements.txt /requirements.txt

#RUN pip install --upgrade pip \
#    && pip install -r requirements.txt

WORKDIR /code/

USER 1000:1000
