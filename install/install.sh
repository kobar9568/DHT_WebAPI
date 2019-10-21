#!/bin/sh

cd `dirname $0`

sudo mkdir /opt/DHT_WebAPI/
sudo cp -r ../src/* /opt/DHT_WebAPI/

sudo apt install python3-venv
sudo python3 -m venv /opt/DHT_WebAPI/venv

. /opt/DHT_WebAPI/venv/bin/activate
sudo /opt/DHT_WebAPI/venv/bin/pip install flask Adafruit_DHT
deactivate

sudo cp dhtd.service /etc/systemd/system/dhtd.service
sudo chown root /etc/systemd/system/dhtd.service
sudo chgrp root /etc/systemd/system/dhtd.service
sudo chmod 644 /etc/systemd/system/dhtd.service

sudo systemctl enable dhtd.service
