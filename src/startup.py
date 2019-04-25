#!/usr/bin/env python3
import sys
sys.path.append('./lib')
sys.path.append('/home/pi/boatshantiesapi/src/lib/')
import RPi.GPIO as GPIO
import pins
import led
import servo
import motion
from time import sleep

print('Hello World!')

led.led_toggle(led.LED.FRONT, led.STATE.ON)
sleep(1)
led.led_toggle(led.LED.FRONT, led.STATE.OFF)

led.led_toggle(led.LED.BACK, led.STATE.ON)
sleep(1)
led.led_toggle(led.LED.BACK, led.STATE.OFF)

led.led_toggle(led.LED.LEFT, led.STATE.ON)
sleep(1)
led.led_toggle(led.LED.LEFT, led.STATE.OFF)

led.led_toggle(led.LED.RIGHT, led.STATE.ON)
sleep(1)
led.led_toggle(led.LED.RIGHT, led.STATE.OFF)

sleep(1)

