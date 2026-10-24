from machine import Pin
from dht import DHT11
import network
from umqtt.simple import MQTTClient
import time

# 配置信息，使用时修改
WIFI_SSID = "你的WiFi名称"
WIFI_PASS = "你的WiFi密码"
MQTT_SERVER = "127.0.0.1"
MQTT_TOPIC = "iot/sensor/temp_hum"

# 初始化DHT11传感器，GPIO4
dht = DHT11(Pin(4))

def connect_wifi():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        print("正在连接WiFi...")
        wlan.connect(WIFI_SSID, WIFI_PASS)
        while not wlan.isconnected():
            time.sleep(0.5)
    print("WiFi连接成功，IP：", wlan.ifconfig()[0])
    return wlan

def mqtt_connect():
    client = MQTTClient("esp32_sensor_01", MQTT_SERVER)
    client.connect()
    print("MQTT连接成功")
    return client

# 主循环
while True:
    try:
        connect_wifi()
        client = mqtt_connect()
        dht.measure()
        temp = dht.temperature()
        hum = dht.humidity()
        payload = '{"temp":%d,"hum":%d}' % (temp, hum)
        client.publish(MQTT_TOPIC, payload)
        print("上报数据：", payload)
        time.sleep(5)
    except Exception as e:
        print("出错，等待重连：", e)
        time.sleep(2)
