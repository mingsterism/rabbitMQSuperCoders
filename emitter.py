import pika
import sys
import json
import common
import configparser
config = configparser.ConfigParser()
config.read('profiles.ini')


q = common.Connector(config['profile1'])
# q = common.Connector('guest', '192.168.1.10', 5672)
# credentials = pika.PlainCredentials('guest', 'guest')
# parameters = pika.ConnectionParameters('192.168.1.13', 5672, '/', credentials)
# connection = pika.BlockingConnection(parameters)
message = json.dumps({'url': 'http://hello.com?1'})
# channel1 = common.create_channel(q, 'logs', 'fanout')
channel1 = common.create_channel(config['profile1'])
channel1.basic_publish(exchange='logs', routing_key='', body=message)
print(" [x] Sent %r" % message)
channel1.close()


#connection = pika.BlockingConnection(pika.ConnectionParameters(
#        host='128.199.89.76'))

# channel = connection.channel()

# channel.exchange_declare(exchange='logs',
#                          type='fanout')

# message = json.dumps({'url': 'http://hello.com?1'})
# channel.basic_publish(exchange='logs',
#                       routing_key='',
#                       body=message)
# print(" [x] Sent %r" % message)
# connection.close()





