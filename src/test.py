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

servo.servo_toggle(servo.SERVO.LEFT, servo.STATE.CW)
servo.servo_toggle(servo.SERVO.LEFT, servo.STATE.CCW)

servo.servo_toggle(servo.SERVO.RIGHT, servo.STATE.CW)
servo.servo_toggle(servo.SERVO.RIGHT, servo.STATE.CCW )

print("FRONT LED")
led.led_toggle(led.LED.FRONT, led.STATE.ON)
sleep(3)

print("TESTING FORWARD")
led.led_toggle(led.LED.FRONT, led.STATE.OFF)
motion.toggle_direction(motion.MOVE.FORWARD)

print("BACK LED")
led.led_toggle(led.LED.BACK, led.STATE.ON)
sleep(3)

print("TESTING BACK")
led.led_toggle(led.LED.BACK, led.STATE.OFF)
motion.toggle_direction(motion.MOVE.BACK)

print("LEFT LED")
led.led_toggle(led.LED.LEFT, led.STATE.ON)
sleep(3)

print("TESTING LEFT")
led.led_toggle(led.LED.LEFT, led.STATE.OFF)
motion.toggle_direction(motion.MOVE.LEFT)

print("RIGHT LED")
led.led_toggle(led.LED.RIGHT, led.STATE.ON)
sleep(3)

print("TESTING RIGHT")
led.led_toggle(led.LED.RIGHT, led.STATE.OFF)
motion.toggle_direction(motion.MOVE.RIGHT)
sleep(3)

