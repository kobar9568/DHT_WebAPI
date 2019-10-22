# DHT_WebAPI

Raspberry PiのGPIOに接続したDHTセンサーの値にWebAPIからアクセス。

## Description

GPIOに接続したDHTセンサーの情報をLAN内の別のコンピューターから利用する為のWebAPI。

## Requirement

* Flask
* Adafruit_DHT

## Installation

### Dependencies

```
pip install Flask Adafruit_DHT
```

### systemd daemon (Experimental)

```
cd install/
chmod u+x install.sh
./install.sh
```

## Usage

```
./app.py &
curl localhost:8080/thermohygrometer

{"humidity":67.6,"temperature":23.9}
```

* Direct

```
sudo systemctl start dhtd
curl localhost:8080/thermohygrometer

{"humidity":67.6,"temperature":23.9}
```

* systemd daemon

## Note

* DHTセンサーが接続されているGPIOピンの設定はsrc/app.pyのGPIO_PINを編集することで可能。デフォルトはGPIO 4(BCM)
* Flask内蔵のWebサーバーを利用している為、本格的な運用には向かない。
* 使用は安全なネットワーク内部に限る。
