from machine import Pin, I2C, Timer
from ssd1306 import SSD1306_I2C
import framebuf

import time
from rotary_irq import RotaryIRQ

WIDTH = 128
HEIGHT = 64
I2C = I2C(0)

#Uses I2C defaults for I2C0 SCL=Pin(GP9), SDA=Pin(GP8)
oled - SSD1306_I2C(WIDTH, HEIGHT, i2c)

r = RotaryIRQ_I2C(pin_num_clk=15,
                  pin_num_dt=14,
                  min_val=0,
                  max_val=20,
                  reverse=False,
                  range_mode=RotaryIRQ.RANGE_BOUNDED)