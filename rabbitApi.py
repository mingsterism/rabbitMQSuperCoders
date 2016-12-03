import consumer
import pika
import sys
import json
import common
import configparser

from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    '''config = configparser.ConfigParser()
    config.read('profiles.ini')

    q = common.Connector(config['profile1'])
    message = json.dumps({'url': 'http://hello.com?1'})
    channel1 = common.create_channel(config['profile1'])
    channel1.basic_publish(exchange=config['profile1']['exchange'], routing_key='', body=message)
    channel1.close()
    return " [x] Sent %r" % message
    '''
    return "Bye bye world"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8001, debug=False)
