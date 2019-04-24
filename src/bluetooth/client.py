#!/usr/bin/env python3
# http://recolog.blogspot.com/2013/07/transferring-files-via-bluetooth-using.html
# lightblue.sourceforge.net
# sudo apt-get install python-bluez libbluetooth-dev python-dev
# "                  " bluez
# "                  " python-bluez libbluetooth-dev python-dev
# sudo python setup.py install

import socket

target_names = [["ACTUALLYNOTHING", 6969]] #put MAC addresses
file_to_send = "behavior.py"
file_time = "time.txt"

# search might miss devices or be unable to connect, so it may need multiple attempts
for target in target_names:
    s = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
    s.connect((target[0], target[1]))
    while 1:
        try:
            f = open(file_time, 'r')
            file = f.read(8)
            s.send(file)
            f.close()
            print("Sent time file")
        except:
            print("An error occured sending time file")
        try:
            f = open(file_to_send, 'r')
            file = f.read(1024)
            while file:
                s.send(file)
                file = f.read(1024)
            f.close()
            print("Sent process file")
        except:
            print("An error occured sending process file")
    s.close()
