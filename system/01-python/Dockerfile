### BUILDER ###

FROM python:3.8.3-alpine as builder

# set work directory
WORKDIR /usr/src/

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install python dependencies
RUN apk update \
    && apk add --no-cache --virtual build-dependencies gcc postgresql-dev python3-dev musl-dev

# install dependencies
RUN pip install --upgrade pip
RUN pip install flake8

# install python dependencies
RUN mkdir ./system
COPY /system/01-python/requirements.txt ./system/
RUN pip wheel --no-cache-dir --no-deps --wheel-dir ./system/wheels -r ./system/requirements.txt

# copy project
COPY /api ./api
RUN flake8 --ignore=E501,F401 ./api/blog

### FINAL ###

FROM python:3.8.3-alpine

WORKDIR /usr/src/

RUN mkdir ./system

## install dependecies
RUN apk add --update --no-cache libpq make curl nano mc bash

COPY --from=builder /usr/src/system/wheels ./system/wheels
COPY --from=builder /usr/src/system/requirements.txt ./system
RUN pip install --upgrade pip
RUN pip install --no-cache ./system/wheels/*

# copy entrypoint.sh
COPY /system/01-python/entrypoint.sh ./system/
COPY /system/wait-for.sh ./system/
RUN chmod +x ./system/wait-for.sh

COPY /api ./api

RUN mkdir -p ./api/static
RUN mkdir -p ./api/media

# change permission to the project folder
WORKDIR /usr/src/api
RUN chmod 755 .

# run entrypoint.sh
ENTRYPOINT ["/usr/src/system/entrypoint.sh"]
