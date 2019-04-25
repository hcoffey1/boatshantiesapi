import time
import sys
sys.path.append("lib")
import led, servo, sensors


def get_front_sensor():
    return sensors.front_value()

def get_left_sensor():
    return sensors.left_value()

def get_right_sensor():
    return sensors.right_value()

def get_back_sensor():
    return sensors.back_value()

def turn(angle=0):
    if angle == 0:
        return
    if angle > 0:
        # We want to turn CCW
        servo.servo_toggle(servo.SERVO.LEFT, servo.STATE.CCW)
        servo.servo_toggle(servo.SERVO.RIGHT, servo.STATE.CCW)
    elif angle < 0:
        servo.servo_toggle(servo.SERVO.LEFT, servo.STATE.CW)
        servo.servo_toggle(servo.SERVO.RIGHT, servo.STATE.CW)
    time.sleep(1)
    servo.servo_toggle(servo.SERVO.LEFT, servo.STATE.HALT)
    servo.servo_toggle(servo.SERVO.RIGHT, servo.STATE.HALT)

def drive(distance=0):
    if distance > 0:
        servo.servo_toggle(servo.SERVO.LEFT, servo.STATE.CW)
        servo.servo_toggle(servo.SERVO.RIGHT, servo.STATE.CCW)
        time.sleep(1)
        servo.servo_toggle(servo.SERVO.LEFT, servo.STATE.HALT)
        servo.servo_toggle(servo.SERVO.RIGHT, servo.STATE.HALT)

def change_signal(light_intensity=0):
    if light_intensity > 0.5:
        led.led_toggle(led.LED.FRONT, led.STATE.ON)
        led.led_toggle(led.LED.BACK, led.STATE.ON)
        led.led_toggle(led.LED.LEFT, led.STATE.ON)
        led.led_toggle(led.LED.RIGHT, led.STATE.ON)
    else:
        led.led_toggle(led.LED.FRONT, led.STATE.OFF)
        led.led_toggle(led.LED.BACK, led.STATE.OFF)
        led.led_toggle(led.LED.LEFT, led.STATE.OFF)
        led.led_toggle(led.LED.RIGHT, led.STATE.OFF)

def sleep(sleep_time=0):
    time.sleep(sleep_time)
