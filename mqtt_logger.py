import csv
import time
import paramiko
import paho.mqtt.client as mqtt
from datetime import datetime

# Configura tus variables
BROKER = "192.168.1.165"   # Tu IP local
PORT = 1883
TOPIC = "u00/#"            # Reemplaza XX por tu número de usuario
CSV_FILE = "mqtt_log.csv"

# Datos SSH del ESP32 (se usarán cuando esté corriendo, ahora podemos simular)
SSH_IP = "192.168.1.165"
SSH_USER = "esp32"
SSH_PASS = "freertos"

# Callback al recibir mensaje MQTT
def on_message(client, userdata, msg):
    ts = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    topic = msg.topic
    payload = msg.payload.decode()
    print(f"[{ts}] {topic} -> {payload}")
    with open(CSV_FILE, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([ts, topic, payload])

# Conexión MQTT
client = mqtt.Client(protocol=mqtt.MQTTv5)
client.on_message = on_message

client.connect(BROKER, PORT, 60)
client.subscribe(TOPIC, qos=1)

# Encabezado CSV
with open(CSV_FILE, "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["timestamp", "topic", "payload"])

print(f"📡 Escuchando mensajes en {BROKER}:{PORT}, topic '{TOPIC}' (MQTTv5)")
print("Presiona Ctrl+C para detener.")

try:
    client.loop_forever()
except KeyboardInterrupt:
    print("\nFinalizando logger.")
    client.disconnect()
