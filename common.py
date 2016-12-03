import pika
import configparser

# def create_channel(user, exchange, type):
# 	credentials = pika.PlainCredentials(user.credentials, user.credentials)
# 	parameters = pika.ConnectionParameters(user.ip, user.port, '/', credentials)
# 	connection = pika.BlockingConnection(parameters)
# 	channel = connection.channel()
# 	channel.exchange_declare(exchange=exchange, type=type)
# 	return channel

def create_channel(profile1):
	credentials = pika.PlainCredentials(profile1['credentials'], profile1['credentials'])
	parameters = pika.ConnectionParameters(profile1['ip'], profiel1['port'], '/', profile1['credentials'])
	connection = pika.BlockingConnection(parameters)
	channel = connection.channel()
	channel.exchange_declare(exchange=profile1['exchange'], type=profile1['type'])
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