class Connector:
	def __init__(self, profile):
		self.credentials = profile['credentials']
		self.ip = profile['ip']
		self.port = profile['port']