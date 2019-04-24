#!usr/bin/python3
import multiprocessing import Process
import bluetooth
import socket
import signal, psutil
import RPi.GPIO as GPIO
import pins
import os
from time import sleep

print('Hello World!')
GPIO.setmode(GPIO.BCM)
GPIO.setup(pins.LED, GPIO.OUT, initial=GPIO.LOW)
GPIO.output(pins.LED, GPIO.HIGH)
sleep(1)
GPIO.output(pins.LED, GPIO.LOW)

hostMACAddress = 'whatever our mac is' # The MAC address of a Bluetooth adapter on the server. The server might have multiple Bluetooth adapters.
port = 3
backlog = 1
size = 1024
s = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
s.bind((hostMACAddress, port))
s.listen(backlog)

def child():
    print("Hes going to fucking destroy me!")
    time.wait(15)
    print("he hasnt yet?")
    # execfile(simulation.py)
    return

def ALEX_JONES():
    p = process(target = child)
    p.start()
    # run child process and check every 10 seconds to see if it is time to end the simulation
    parent = psutil.Process(os.pid)
    children = parent.children(recursive=True)
    os.wait(5) 
    for process in children:
        process.send_signal(signal.SIGTERM)

def main(): 
    try:
        client, clientInfo = s.accept()
        with open('simulation.json', 'w+') as f:
            while 1:
                data = client.recv(size)
                if data:
                    f.write(data)
                    print(data)
                else:
                    break
        aj = process(target = ALEX_JONES)
        aj.start()
    except: 
        print("Closing socket")
        client.close()
        s.close()
    return


if __name__ = "__main__":
    main()
