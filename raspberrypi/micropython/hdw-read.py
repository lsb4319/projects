from machine import I2C, Pin
import time, struct

i2c = I2C(0, sda=Pin(0), scl=Pin(1), freq=100000)
ADDR, OSS = 0x77, 3  # OSS 0-3 = oversampling (3 = highest resolution)

AC1,AC2,AC3,AC4,AC5,AC6,B1,B2,MB,MC,MD = struct.unpack(
    '>hhhHHHhhhhh', i2c.readfrom_mem(ADDR, 0xAA, 22))

def read():
    # temperature
    i2c.writeto_mem(ADDR, 0xF4, b'\x2E'); time.sleep_ms(5)
    UT = struct.unpack('>H', i2c.readfrom_mem(ADDR, 0xF6, 2))[0]
    # pressure
    i2c.writeto_mem(ADDR, 0xF4, bytes([0x34 + (OSS << 6)])); time.sleep_ms(26)
    m, l, x = i2c.readfrom_mem(ADDR, 0xF6, 3)
    UP = ((m << 16) + (l << 8) + x) >> (8 - OSS)

    X1 = ((UT - AC6) * AC5) >> 15
    X2 = int((MC << 11) / (X1 + MD))
    B5 = X1 + X2
    temp = ((B5 + 8) >> 4) / 10

    B6 = B5 - 4000
    X1 = (B2 * ((B6 * B6) >> 12)) >> 11
    X2 = (AC2 * B6) >> 11
    B3 = ((((AC1 * 4) + X1 + X2) << OSS) + 2) // 4
    X1 = (AC3 * B6) >> 13
    X2 = (B1 * ((B6 * B6) >> 12)) >> 16
    X3 = (X1 + X2 + 2) >> 2
    B4 = (AC4 * (X3 + 32768)) >> 15
    B7 = (UP - B3) * (50000 >> OSS)
    p = (B7 * 2) // B4 if B7 < 0x80000000 else (B7 // B4) * 2
    X1 = ((p >> 8) * (p >> 8) * 3038) >> 16
    X2 = (-7357 * p) >> 16
    p += (X1 + X2 + 3791) >> 4

    alt = 44330 * (1 - (p / 101325) ** (1 / 5.255))
    return temp, p, alt

while True:
    t, p, a = read()
    print(f"{t:.1f} °C  {p/100:.2f} hPa  ~{a:.0f} m")
    time.sleep(2)