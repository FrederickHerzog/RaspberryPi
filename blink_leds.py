#Frederick Herzog
#blinks one or more led's 

import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)

def gpio_setup(lst):
  for led in lst:
	  GPIO.setup(led, GPIO.OUT)

def led_on(x):
  GPIO.output(x, True)
 
def led_off(x):
  GPIO.output(x, False)

def blink(led, n, pause_t):
  for i in range(n):
	  led_on(led)
		sleep(pause_t)
		led_off(led)
		sleep(pause_t)

led1 = 18
leds = [led1]
num_blinks = 30
pause = .09
gpio_setup(leds)

for led in leds:
	blink(led, num_blinks, pause)
