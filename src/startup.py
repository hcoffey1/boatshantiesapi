#!/usr/bin/env python3
import sys
sys.path.append('./lib')
import RPi.GPIO as GPIO
import pins
import led
from time import sleep

print('Hello World!')
GPIO.setmode(GPIO.BCM)

led.led_init()

led.led_toggle(led.LED.FRONT, led.STATE.ON)
sleep(1)
led.led_toggle(led.LED.FRONT, led.STATE.OFF)
