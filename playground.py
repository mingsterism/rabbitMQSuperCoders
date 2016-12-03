import configparser
config = configparser.ConfigParser()
config.read('profiles.ini')
print(config['profile1']['ip'])