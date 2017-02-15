# rabbitMQSuperCoders
Data streaming between rabbitmq container and psql container on docker network bridge. 

todo
- fix up docker-compose.yml file
- create postgresql container and link with rabbitmq container data stream
- auto expose ports to allow data stream 

### Run
docker build -t rabbitServer1 .
docker run -it --name rabbitContainer1 <br> --network=testnetwork rabbitServer1 
