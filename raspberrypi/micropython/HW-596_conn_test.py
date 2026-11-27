from machine import I2C, Pin
i2c = I2C(0, sda=Pin(0), scl=Pin(1), freq=100000)
print([hex(a) for a in i2c.scan()])   # should print ['0x77']