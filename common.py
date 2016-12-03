import pika
import configparser

# def create_channel(user, exchange, type):
# 	credentials = pika.PlainCredentials(user.credentials, user.credentials)
# 	parameters = pika.ConnectionParameters(user.ip, user.port, '/', credentials)
# 	connection = pika.BlockingConnection(parameters)
# 	channel = connection.channel()
# 	channel.exchange_declare(exchange=exchange, type=type)
# 	return channel

def create_channel(p):
	credentials = pika.PlainCredentials(p['credentials'], p['credentials'])
	parameters = pika.ConnectionParameters(p['ip'], int(p['port']), '/', credentials)
	connection = pika.BlockingConnection(parameters)
	channel = connection.channel()
	channel.exchange_declare(exchange=p['exchange'], type=p['type'])
	return channel

# class Connector:
	# def __init__(self, credentials, ip, port):
	# 	self.credentials = credentials
	# 	self.ip = ip
	# 	self.port = port

class Connector:
	def __init__(self, profile):
		self.credentials = profile['credentials']
		self.ip = profile['ip']
		self.port = profile['port']
