#!/usr/bin/env python3
import RPi.GPIO as GPIO
import pins
from time import sleep

print('Hello World!')
GPIO.setup(pins.LED, GPIO.OUT, initial=GPIO.LOW)
GPIO.output(pins.LED, GPIO.HIGH)
sleep(1)
GPIO.output(pins.LED, GPIO.LOW)
