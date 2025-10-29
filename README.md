# 🛰️ MQTT v5 con Broker Local y ESP32 (FreeRTOSCourse)

## 📘 Descripción

Este proyecto implementa una comunicación IoT completa utilizando el protocolo **MQTT v5**, un **broker local Mosquitto**, un **cliente Python** (`mqtt_logger.py`), y una **ESP32** corriendo FreeRTOS (contenedor FreeRTOSCourse).  
El sistema permite publicar y registrar datos de sensores, verificando la interoperabilidad entre un dispositivo embebido y un cliente local en Linux.

---

## 🧩 Estructura del Proyecto

workspace/
├── mqtt5/ # Proyecto ESP-IDF para la ESP32
├── mqtt_logger.py # Cliente Python (Paho MQTT v5 + CSV)
├── mqtt_log.csv # Archivo generado con los datos
└── README.md # Este documento


---

## 🛠️ Requerimientos

- **Ubuntu Linux**
- **Docker con FreeRTOSCourse** (ESP-IDF)
- **ESP32 DevKit v1**
- **Python 3.12**
- **Librerías:**
  ```bash
  paho-mqtt==2.1.0
  paramiko==3.5.0
Broker MQTT: Mosquitto (MQTT v5)


