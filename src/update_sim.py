import bluetooth
import sys

port = 9998
devices = bluetooth.discover_devices()
proc_list = []
for addr in devices:
    print(addr)
    s = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
    s.connect((addr, port))
    filename = sys.argv[1]
    with open(filename, 'r') as f:
        buf = f.read().encode('utf-8')
        s.send(buf)
    s.close()
