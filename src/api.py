from lib import led
import time


def get_front_sensor():
    return 0

def get_left_sensor():
    return 0

def get_right_sensor():
    return 0

def get_back_sensor():
    return 0

def turn(angle=0):
    pass

def drive(distance=0):
    pass

def change_signal(light_intensity=0):
    if light_intensity > 0.5:
        led_toggle(LED.FRONT, STATE.ON)
        led_toggle(LED.BACK, STATE.ON)
        led_toggle(LED.LEFT, STATE.ON)
        led_toggle(LED.RIGHT, STATE.ON)
    else:
        led_toggle(LED.FRONT, STATE.OFF)
        led_toggle(LED.BACK, STATE.OFF)
        led_toggle(LED.LEFT, STATE.OFF)
        led_toggle(LED.RIGHT, STATE.OFF)

def sleep(sleep_time=0):
    time.sleep(sleep_time)
