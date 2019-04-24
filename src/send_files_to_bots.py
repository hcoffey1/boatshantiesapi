#!/usr/bin/env python3
# lightblue.sourceforge.net
# sudo apt-get install python-bluez libbluetooth-dev python-dev
# "                  " bluez
# "                  " python-bluez libbluetooth-dev python-dev
# sudo python setup.py install

import bluetooth
import lightblue
import socket


def main():
    target_names = [] #put bluetooth names
    file_to_send = "behavior.py"

    target_address = None
    nearby_devices = bluetooth.discover_devices()

    for target in target_names:
        for bdaddr in nearby_devices:
            if target_name == bluetooth.lookup_name(bdaddr):
                print("found the device")
                target_address = bdaddr
                break

        services = lightblue.findservices(target_address)
        for service in services:
            if service[2] == "OBEX Object Push":
                obex_port = service[1]
                break

        try:
            lightblue.obex.sendfile(target_address, service[1], file_to_send)
        except:
            print("An error occured connecting to file")

if __name__ == "__main__":
    exit(main())

