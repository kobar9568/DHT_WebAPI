#!/usr/bin/env python3

import sys
import time
from decimal import Decimal, ROUND_HALF_UP
import Adafruit_DHT


def order_sensing(gpio_pin):
    """
    GPIOに装着されたDHT22から温度と湿度を取得する。

    Parameters
    ----------
    gpio_pin : int
        DHT22が接続されているGPIOのBCMピン番号

    Returns
    -------
    temperature, humidity : tuple of float
        温度と湿度のタプル。センサーからの取得に失敗した場合は共に0.0を返す。
    """
    humidity, temperature = Adafruit_DHT.read_retry(Adafruit_DHT.DHT22, gpio_pin)

    if temperature is not None and humidity is not None:
        temperature = float(Decimal(str(temperature)).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP))
        humidity = float(Decimal(str(humidity)).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP))

        return (temperature, humidity)
    else:
        return (0.0, 0.0)


if __name__ == '__main__':
    args = sys.argv
    del args[0]

    if not len(args) == 1:
        print('usage : fetch_dht22.py BCM_GPIO_Number')

    gpio_pin = args[0]

    temperature, humidity = order_sensing(gpio_pin)
    if temperature == 0.0 and humidity == 0.0:
        print('Failed to get value from sensor.')
    else:
        print(temperature, humidity)
