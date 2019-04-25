#!usr/bin/python3
from multiprocessing import Process
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

#hostMACAddress = 'whatever our mac is' # The MAC address of a Bluetooth adapter on the server. The server might have multiple Bluetooth adapters.
port = 9999
backlog = 1
size = 1024
s = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
s.bind(("", port))
s.listen(backlog)

def child():
    print("Hes going to fucking destroy me!")
    #time.wait(15)
    #print("he hasnt yet?")
    # execfile(simulation.py)
    return

def ALEX_JONES():
    p = process(target = child)
    p.start()
    # run child process and check every 10 seconds to see if it is time to end the simulation
    os.wait(5)

    # should never get here
    p.join()
    p.terminate()

def main():
    while 1:
        try:
            client = s.accept()
        except:
            print("Closing socket")
            client.close()
            s.close()
        with open('simulation.json', 'w+') as f:
            data = client.recv(size)
            while len(data) != 0:
                #print(data)
                f.write(data)
                data = client.recv(size)

            print("wrote new json file")
            return;
        #aj = process(target = ALEX_JONES)
        #aj.start()
    return


if __name__ == "__main__":
    main()
