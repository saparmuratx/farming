FROM python:3.10.6

ENV PYTHON_VERSION=3.10.6
ENV PYTHONBUFFERED 1

RUN apt-get update -qq && apt-get install -y -qq \
    # std libs
    git less nano curl \
    ca-certificates \
    wget build-essential\
    # geodjango
    gdal-bin binutils libproj-dev libgdal-dev \
    python3-gdal*

RUN mkdir /farming

WORKDIR /farming

ADD . /farming/

RUN pip install -r requirements.txt
