import paho.mqtt.client as mqtt
import sqlite3
import json
import time

# 初始化数据库
conn = sqlite3.connect("sensor.db", check_same_thread=False)
cur = conn.cursor()
cur.execute('''CREATE TABLE IF NOT EXISTS data (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    temp REAL,
    hum REAL,
    ts DATETIME DEFAULT CURRENT_TIMESTAMP
)''')
conn.commit()

def on_message(client, userdata, msg):
    try:
        payload = json.loads(msg.payload.decode())
        temp = payload["temp"]
        hum = payload["hum"]
        print(f"收到数据：温度 {temp}℃，湿度 {hum}%")
        cur.execute("INSERT INTO data(temp, hum) VALUES (?, ?)", (temp, hum))
        conn.commit()
    except Exception as e:
        print("解析失败：", e)

client = mqtt.Client()
client.on_message = on_message
client.connect("127.0.0.1", 1883, 60)
client.subscribe("iot/sensor/temp_hum")
print("后端订阅服务启动，等待ESP32上报数据...")
client.loop_forever()
