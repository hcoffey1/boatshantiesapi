import bluetooth
import sys

port = 9998
s = bluetooth.BluetoothSocket(bluetooth.RFCOMM)

devices = bluetooth.discover_devices()
for addr in devices:
    print(addr)
    s.connect((addr, port))
    filename = sys.argv[1]
    with open(filename) as f:
        buf = f.read().encode('utf-8')
        s.send(buf)
    s.close()
