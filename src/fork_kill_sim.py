#!usr/bin/python3
from multiprocessing import Process
import bluetooth
import os

port = 9998
backlog = 1
size = 1024
SIM_FILE="/tmp/sim.json"
s = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
s.bind(("", port))
s.listen(backlog)

def child():
    print("Hes going to fucking destroy me!")
    return

def main():
    p = Process(target = child)
    p.start()
    while 1:
        client = s.accept()[0]

        p.terminate()
        with open(SIM_FILE, 'w+') as f:
            f.truncate()
            while 1:
                try:
                    data = client.recv(size)
                except:
                    break
                if not data:
                    break

                f.write(data.decode())

            print("wrote new json file, restarting simulation")
            p = Process(target = child)
            p.start()

    #should never get here
    s.close()
    return

if __name__ == "__main__":
    main()
