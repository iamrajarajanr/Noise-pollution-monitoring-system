import paho.mqtt.client as mqtt
import time
from noise_sensor_library import read_noise_level  # Replace with actual library or sensor code

# Sensor configuration
sensor_id = "sensor_1"
sensor_location = "Public Area 1"
mqtt_broker = "your_mqtt_broker"
mqtt_port = 1883
topic = "noise_data"

# Initialize MQTT client
client = mqtt.Client(sensor_id)
client.connect(mqtt_broker, mqtt_port)

while True:
    # Read noise level from the sensor
    noise_level = read_noise_level()

    # Create a JSON payload with sensor data
    payload = {
        "sensor_id": sensor_id,
        "location": sensor_location,
        "noise_level_dB": noise_level,
        "timestamp": int(time.time())
    }

    # Publish data to the MQTT topic
    client.publish(topic, json.dumps(payload))

    time.sleep(60)  # Adjust the interval as needed
