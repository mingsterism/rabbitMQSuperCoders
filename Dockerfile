FROM ubuntu:16.04
MAINTAINER Ming "ming.k@hotmail.com"
RUN apt-get -y update
RUN apt-get -y upgrade
RUN apt-get -y install sudo
RUN echo 'Updates have been done...'
RUN echo 'Installing essential libraries now...'
RUN apt-get -y install python3
RUN apt-get -y install python3-pip
RUN apt-get -y install libpq-dev
RUN pip3 install psycopg2
EXPOSE 5432 8001 8002 80
CMD echo 'hey welcome to my container'
CMD mkdir /home/myworkdspace

