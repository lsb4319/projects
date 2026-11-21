# main.py - read a BMP180 (GY-68) on a Pico W
# Wiring: VIN -> 3V3(OUT) pin 36, GND -> GND, SDA -> GP4 (pin 6), SCL -> GP5 (pin 7)

from machine import Pin, I2C
import time
from bmp180 import BMP180

i2c = I2C(0, sda=Pin(4), scl=Pin(5), freq=100000)
print("I2C devices found:", [hex(a) for a in i2c.scan()])  # expect ['0x77']

sensor = BMP180(i2c, oversampling=3)
# For accurate altitude, set today's local sea-level pressure (in Pa), e.g. 1018.2 hPa -> 101820
# sensor.sea_level_pa = 101820

while True:
    try:
        temp_c, pressure_pa = sensor.read()
        temp_f = temp_c * 9 / 5 + 32
        hpa = pressure_pa / 100
        inhg = pressure_pa / 3386.39
        alt_m = sensor.altitude(pressure_pa)
        print(f"Temp: {temp_c:.1f}°C / {temp_f:.1f}°F   "
              f"Pressure: {hpa:.1f} hPa / {inhg:.2f} inHg   "
              f"Altitude: ~{alt_m:.0f} m")
    except OSError as e:
        print("Read failed:", e)
    time.sleep(300)
