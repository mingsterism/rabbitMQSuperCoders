def create_channel(user, exchange, type):
	credentials = pika.PlainCredentials(user.credentials)
	parameters = pika.ConnectionParameters(user.ip, user.port, '/', credentials)
	connection = pika.BlockingConnection(parameters)
	channel = connection.channel()
	channel.exchange_declare(exchange=exchange, 
							type=type)
	return channel
	
class Connector:
	def __init__(self, credentials, ip, port):
		self.credentials = credentials
		self.ip = ip
		self.port = port
