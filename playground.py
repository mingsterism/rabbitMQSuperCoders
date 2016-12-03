import configparser
import playground2


config = configparser.ConfigParser()
config.read('profiles.ini')
print(config['profile1']['ip'])
# print(config['profile1']['credentials'])
a = playground2.Connector(config['profile1'])