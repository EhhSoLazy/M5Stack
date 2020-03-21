from m5stack import *
from m5ui import *
from uiflow import *
import machine
import utime
import amg8833
import math

label0 = M5TextBox(0, 0, "Text", lcd.FONT_Default,0xFFFFFF, rotate=0)
sensor = amg88xx.AMG8833()
utime.sleep(.1)

while True:
    utime.sleep(0.2)
    #read the pixels
    pixels = sensor.read_temp()
    #print(pixels)
    label0.setText(str(pixels))