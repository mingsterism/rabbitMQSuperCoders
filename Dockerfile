FROM ubuntu:16.04
MAINTAINER Ming "ming.k@hotmail.com"
RUN apt-get -y update && apt-get -y upgrade
RUN apt-get -y install sudo
RUN echo 'Updates have been done...'
RUN echo 'Installing essential libraries now...'
RUN apt-get -y install \
	python3	\
	python3-pip \
	libpq-dev \
	wget \
	git
RUN pip3 install psycopg2

RUN echo 'deb http://www.rabbitmq.com/debian/ testing main' | \
        sudo tee /etc/apt/sources.list.d/rabbitmq.list
RUN wget -O- https://www.rabbitmq.com/rabbitmq-release-signing-key.asc | \
        sudo apt-key add -
RUN apt-get -y update && apt-get -y install rabbitmq-server

# Copying base config files for rabbitmq. Allow guests to receive from remote users
RUN git clone https://github.com/mingsterism/rabbitMQSuperCoders /home/rabbitMQ
COPY rabbitmqConfig/rabbitmq.config /etc/rabbitmq/rabbitmq.config
RUN rabbitmq-server 

ENV rabbitDir /home/rabbitMQ
WORKDIR $rabbitDir
RUN rabbitmqctl status
EXPOSE 5432 8001 8002 80


