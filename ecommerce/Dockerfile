# Get the image
FROM python:2.7

MAINTAINER Parikshit Yadav <parikshit979@gmail.com>

# Install apt packages
RUN apt-get update && apt-get install -y python-dev && apt-get install -y python-pip \
    && apt-get install -y default-libmysqlclient-dev && apt-get install -y supervisor \
    && apt-get install -y python-setuptools

# Copy services supervisor config files
COPY ./ecommerce.conf /etc/supervisor/conf.d/ecommerce.conf

# Add source code
ADD . /ecommerce/

COPY ./requirements.txt /ecommerce/requirements.txt

WORKDIR /ecommerce/

RUN pip install --upgrade setuptools pip
RUN pip install -r requirements.txt
