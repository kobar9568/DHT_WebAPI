#!/usr/bin/env python3

from flask import Flask, jsonify
from dht import order_sensing

GPIO_PIN = 4 # DHT22 GPIO pin number (BCM)

app = Flask(__name__)


@app.route('/thermohygrometer')
def respond():
    temperature, humidity = order_sensing(GPIO_PIN)
    return jsonify({'temperature': temperature, 'humidity': humidity})


if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=8080)
