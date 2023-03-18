FROM python:3.8

ENV PYTHONBUFFERED=1
ENV DEBIAN_FRONTEND noninteractive

LABEL maintainer="Chriford Siame <siamechrif@gmail.com>"

RUN export DEBIAN_FRONTEND=noninteractive
RUN dpkg-divert --local --rename --add /sbin/initctl

RUN apt-get update -y

# Install apt packages
RUN apt-get update && apt-get install -y python3-pip && \
  apt-get install --no-install-recommends -y \
  # dependencies for building Python packages
  build-essential \
  # psycopg2 dependencies
  libpq-dev \
  binutils \
  python3-setuptools \
  libproj-dev \
  rpl \
  # # DGDAL dependencie
  # libproj-dev \
  gdal-bin && \
  apt-get install -y libgeos-dev libgdal-dev && \
  apt-get install -y --reinstall build-essential \
  # cleaning up unused files
  && apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false \
  && rm -rf /var/lib/apt/lists/* \
  && apt-get -y update && \
  apt-get -y auto-remove

COPY ./requirements.txt .
RUN pip install -r requirements.txt
COPY . /app
WORKDIR /app

COPY ./entrypoint.sh /
ENTRYPOINT [ "sh", "/entrypoint.sh" ]
