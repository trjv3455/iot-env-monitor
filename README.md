# iot-env-monitor
# ESP32 MQTT 环境监测系统
> IoT全链路练习项目，包含设备采集、MQTT消息传输、数据存储与可视化

## 🛠 技术栈
- 设备端：ESP32 + MicroPython，DHT11/DHT22温湿度传感器
- 消息中间件：Mosquitto MQTT Broker
- 后端：Python paho-mqtt、SQLite
- 可视化：Grafana

> ⚠️ 重要说明：`firmware/` 目录下为ESP32专用MicroPython固件代码，依赖嵌入式专属库（machine / network / dht），**不能直接在电脑普通Python环境运行，需要烧录进ESP32开发板**。backend目录下脚本为PC端可直接运行的后端服务。

## ✨ 功能
1. 定时采集环境温湿度，封装JSON格式报文
2. ESP32自动连接WiFi，断网自动重连，稳定上报MQTT
3. Python服务订阅MQTT主题，解析数据并入库
4. Grafana绘制实时曲线，支持配置温湿度阈值告警

## 📂 目录结构
iot-env-monitor/
├── firmware/        # ESP32 MicroPython 固件代码（硬件烧录使用）
├── backend/         # Python 订阅、存储脚本（PC 端运行）
├── docker/          # docker-compose 一键启动 mqtt+grafana
├── docs/            # 架构图、接线图、演示 GIF
└── README.md

## 🚀 快速部署
1. 启动Mosquitto、Grafana服务
```bash
docker-compose up -d
