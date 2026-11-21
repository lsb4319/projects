from machine import Pin
import dht, time

sensor = dht.DHT11(Pin(15))
while True:
    try:
        sensor.measure()
        print(f"Temperature: {sensor.temperature()}°C, Humidity: {sensor.humidity()}% ")
    except OSError as e:
        print("Failed to read sensor.", e)
    time.sleep(300)