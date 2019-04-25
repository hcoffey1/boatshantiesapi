import bluetooth
import sys

port = 9998
devices = bluetooth.discover_devices(lookup_names=True)
proc_list = []
for addr,name in devices:
    print(addr + " - " + name)
    s = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
    try:
        s.connect((addr, port))
    except:
        print("couldn't connect to " + addr)
        continue
    filename = sys.argv[1]
    with open(filename, 'r') as f:
        buf = f.read().encode('utf-8')
        s.send(buf)
    s.close()
