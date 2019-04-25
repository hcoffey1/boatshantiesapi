#!/usr/bin/env python3
import sys
sys.path.append('./lib')
import RPi.GPIO as GPIO
import pins
import led
import servo
import motion
from time import sleep

print('Hello World!')
GPIO.setmode(GPIO.BCM)

servo.servo_toggle(servo.SERVO.LEFT, servo.STATE.CW)
servo.servo_toggle(servo.SERVO.LEFT, servo.STATE.CCW)

servo.servo_toggle(servo.SERVO.RIGHT, servo.STATE.CW)
servo.servo_toggle(servo.SERVO.RIGHT, servo.STATE.CCW )

led.led_toggle(led.LED.FRONT, led.STATE.ON)
sleep(1)
led.led_toggle(led.LED.FRONT, led.STATE.OFF)

motion.toggle_direction(motion.MOVE.FORWARD)

led.led_toggle(led.LED.BACK, led.STATE.ON)
sleep(1)
led.led_toggle(led.LED.BACK, led.STATE.OFF)

motion.toggle_direction(motion.MOVE.BACK)

led.led_toggle(led.LED.LEFT, led.STATE.ON)
sleep(1)
led.led_toggle(led.LED.LEFT, led.STATE.OFF)

motion.toggle_direction(motion.MOVE.LEFT)

led.led_toggle(led.LED.RIGHT, led.STATE.ON)
sleep(1)
led.led_toggle(led.LED.RIGHT, led.STATE.OFF)

motion.toggle_direction(motion.MOVE.RIGHT)

sleep(1)

