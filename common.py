class Connector:
	def __init__(self, credentials, ip, port):
		self.credentials = credentials
		self.ip = ip
		self.port = port

def parameters(user):
	credentials = pika.PlainCredentials(user.credentials)
	parameters = pika.ConnectionParameters(user.ip, user.port, '/', credentials)
	connection = pika.BlockingConnection(parameters)