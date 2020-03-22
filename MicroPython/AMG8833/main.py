from m5stack import *
from m5ui import *
from uiflow import *
import machine, utime, amg88xx,  math, i2c_bus
setScreenColor(0x222222)
p1 = M5TextBox(0, 0, "Text", lcd.FONT_Default,0xFFFFFF, rotate=0)
p2 = M5TextBox(40, 0, "Text", lcd.FONT_Default,0xFFFFFF, rotate=0)
p3 = M5TextBox(80, 0, "Text", lcd.FONT_Default,0xFFFFFF, rotate=0)
p4 = M5TextBox(120, 0, "Text", lcd.FONT_Default,0xFFFFFF, rotate=0)
p5 = M5TextBox(160, 0, "Text", lcd.FONT_Default,0xFFFFFF, rotate=0)
p6 = M5TextBox(200, 1, "Text", lcd.FONT_Default,0xFFFFFF, rotate=0)
p7 = M5TextBox(240, 0, "Text", lcd.FONT_Default,0xFFFFFF, rotate=0)
p8 = M5TextBox(280, 0, "Text", lcd.FONT_Default,0xFFFFFF, rotate=0)
p9 = M5TextBox(0, 30, "Text", lcd.FONT_Default,0xFFFFFF, rotate=0)
p10 = M5TextBox(40, 30, "Text", lcd.FONT_Default,0xFFFFFF, rotate=0)
p11 = M5TextBox(80, 30, "Text", lcd.FONT_Default,0xFFFFFF, rotate=0)
p12 = M5TextBox(120, 30, "Text", lcd.FONT_Default,0xFFFFFF, rotate=0)
p13 = M5TextBox(160, 30, "Text", lcd.FONT_Default,0xFFFFFF, rotate=0)
p14 = M5TextBox(200, 30, "Text", lcd.FONT_Default,0xFFFFFF, rotate=0)
p15 = M5TextBox(240, 30, "Text", lcd.FONT_Default,0xFFFFFF, rotate=0)
p16 = M5TextBox(280, 30, "Text", lcd.FONT_Default,0xFFFFFF, rotate=0)
p17 = M5TextBox(0, 60, "Text", lcd.FONT_Default,0xFFFFFF, rotate=0)
p18 = M5TextBox(40, 60, "Text", lcd.FONT_Default,0xFFFFFF, rotate=0)
p19 = M5TextBox(80, 60, "Text", lcd.FONT_Default,0xFFFFFF, rotate=0)
p20 = M5TextBox(120, 60, "Text", lcd.FONT_Default,0xFFFFFF, rotate=0)
p21 = M5TextBox(160, 60, "Text", lcd.FONT_Default,0xFFFFFF, rotate=0)
p22 = M5TextBox(200, 60, "Text", lcd.FONT_Default,0xFFFFFF, rotate=0)
p23 = M5TextBox(240, 60, "Text", lcd.FONT_Default,0xFFFFFF, rotate=0)
p24 = M5TextBox(280, 60, "Text", lcd.FONT_Default,0xFFFFFF, rotate=0)
pixel = None
pixel_val = None
pixels = None

while True:
  sensor=amg88xx.AMG8833()
  pixels = sensor.read_temp()
  pixel = 1
  for count in range(64):
    pixel_val = pixels[int(round(pixel) - 1)]
    if pixel == 1:
      p1.setText(str(pixel_val))
    if pixel == 2:
      p2.setText(str(pixel_val))
    if pixel == 3:
      p3.setText(str(pixel_val))
    if pixel == 4:
      p4.setText(str(pixel_val))
    if pixel == 5:
      p5.setText(str(pixel_val))
    if pixel == 6:
      p6.setText(str(pixel_val))
    if pixel == 7:
      p7.setText(str(pixel_val))
    if pixel == 8:
      p8.setText(str(pixel_val))
    if pixel == 9:
      p9.setText(str(pixel_val))
    if pixel == 10:
      p10.setText(str(pixel_val))
    if pixel == 11:
      p11.setText(str(pixel_val))
    if pixel == 12:
      p12.setText(str(pixel_val))
    if pixel == 13:
      p13.setText(str(pixel_val))
    if pixel == 14:
      p14.setText(str(pixel_val))
    if pixel == 15:
      p15.setText(str(pixel_val))
    if pixel == 16:
      p16.setText(str(pixel_val))
    if pixel == 17:
      p17.setText(str(pixel_val))
    if pixel == 18:
      p18.setText(str(pixel_val))
    if pixel == 19:
      p19.setText(str(pixel_val))
    if pixel == 20:
      p20.setText(str(pixel_val))
    if pixel == 21:
      p21.setText(str(pixel_val))
    if pixel == 22:
      p22.setText(str(pixel_val))
    if pixel == 23:
      p23.setText(str(pixel_val))
    if pixel == 24:
      p24.setText(str(pixel_val))
    pixel = (pixel if isinstance(pixel, int) else 0) + 1
  wait_ms(2)

