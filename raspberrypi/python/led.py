from gpiozero import DigitalOutputDevice
from time import sleep

led = DigitalOutputDevice(2)

while True:
    for i in range(3):
        led.on()
        sleep(1)
        led.off()
        sleep(.5)
    for i in range(3):
        led.on()
        sleep(.5)
        led.off()
        sleep(.5)
    for i in range(3):
        led.on()
        sleep(1)
        led.off()
        sleep(.5)
    sleep(2)
    led.off()    
    