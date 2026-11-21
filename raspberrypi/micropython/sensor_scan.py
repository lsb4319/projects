from machine import Pin
import dht, time

time.sleep(2)  # let the sensor power up
for gp in range(29):
    if gp in (23, 24, 25, 29): continue  # used internally on Pico W
    try:
        s = dht.DHT11(Pin(gp))
        s.measure()
        print(f"Found on GP{gp}: {s.temperature()}°C, {s.humidity()}%")
    except OSError:
        pass
print("Scan done")