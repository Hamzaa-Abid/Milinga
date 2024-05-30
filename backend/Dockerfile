# pull official base image
FROM python:3.8.3-slim-buster

# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
# for twisted
RUN apt-get update -y
RUN apt-get upgrade -y
RUN apt-get -y install libffi-dev libssl-dev python python-dev python-pip

RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# copy project
COPY . .