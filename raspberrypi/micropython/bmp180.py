# bmp180.py - minimal MicroPython driver for the Bosch BMP180 (GY-68 board)
# Save this file to the Pico W as "bmp180.py".

import time
import struct

BMP180_ADDR = 0x77


def _div(a, b):
    """Integer division that truncates toward zero, like C (the datasheet math assumes this)."""
    q = abs(a) // abs(b)
    return q if (a >= 0) == (b >= 0) else -q


class BMP180:
    def __init__(self, i2c, addr=BMP180_ADDR, oversampling=3):
        """
        i2c          : a machine.I2C object
        oversampling : 0 (fastest) to 3 (most accurate)
        """
        self.i2c = i2c
        self.addr = addr
        self.oss = max(0, min(3, oversampling))
        self.sea_level_pa = 101325  # set to your local sea-level pressure for accurate altitude

        chip_id = self.i2c.readfrom_mem(self.addr, 0xD0, 1)[0]
        if chip_id != 0x55:
            raise OSError("BMP180 not found (chip id 0x%02X, expected 0x55)" % chip_id)

        cal = struct.unpack(">hhhHHHhhhhh", self.i2c.readfrom_mem(self.addr, 0xAA, 22))
        (self.AC1, self.AC2, self.AC3, self.AC4, self.AC5, self.AC6,
         self.B1, self.B2, self.MB, self.MC, self.MD) = cal

    # --- raw reads -------------------------------------------------------
    def _read_raw_temp(self):
        self.i2c.writeto_mem(self.addr, 0xF4, b"\x2E")
        time.sleep_ms(5)
        msb, lsb = self.i2c.readfrom_mem(self.addr, 0xF6, 2)
        return (msb << 8) | lsb

    def _read_raw_pressure(self):
        self.i2c.writeto_mem(self.addr, 0xF4, bytes([0x34 + (self.oss << 6)]))
        time.sleep_ms((5, 8, 14, 26)[self.oss])
        msb, lsb, xlsb = self.i2c.readfrom_mem(self.addr, 0xF6, 3)
        return ((msb << 16) | (lsb << 8) | xlsb) >> (8 - self.oss)

    # --- datasheet compensation math ------------------------------------
    def _compute_b5(self, ut):
        x1 = ((ut - self.AC6) * self.AC5) >> 15
        x2 = _div(self.MC << 11, x1 + self.MD)
        return x1 + x2

    def _compute_pressure(self, up, b5):
        oss = self.oss
        b6 = b5 - 4000
        x1 = (self.B2 * ((b6 * b6) >> 12)) >> 11
        x2 = (self.AC2 * b6) >> 11
        x3 = x1 + x2
        b3 = _div(((self.AC1 * 4 + x3) << oss) + 2, 4)
        x1 = (self.AC3 * b6) >> 13
        x2 = (self.B1 * ((b6 * b6) >> 12)) >> 16
        x3 = ((x1 + x2) + 2) >> 2
        b4 = (self.AC4 * (x3 + 32768)) >> 15
        b7 = (up - b3) * (50000 >> oss)
        if b7 < 0x80000000:
            p = (b7 * 2) // b4
        else:
            p = (b7 // b4) * 2
        x1 = (p >> 8) * (p >> 8)
        x1 = (x1 * 3038) >> 16
        x2 = (-7357 * p) >> 16
        return p + ((x1 + x2 + 3791) >> 4)

    # --- public API -----------------------------------------------------
    def read(self):
        """Returns (temperature_c, pressure_pa)."""
        b5 = self._compute_b5(self._read_raw_temp())
        temp_c = ((b5 + 8) >> 4) / 10
        pressure_pa = self._compute_pressure(self._read_raw_pressure(), b5)
        return temp_c, pressure_pa

    @property
    def temperature(self):
        return self.read()[0]

    @property
    def pressure(self):
        return self.read()[1]

    def altitude(self, pressure_pa=None):
        """Approximate altitude in metres, based on self.sea_level_pa."""
        if pressure_pa is None:
            pressure_pa = self.pressure
        return 44330 * (1 - (pressure_pa / self.sea_level_pa) ** (1 / 5.255))
