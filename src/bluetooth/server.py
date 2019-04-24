import bluetooth

hostMACAddress = 'whatever our mac is' # The MAC address of a Bluetooth adapter on the server. The server might have multiple Bluetooth adapters.
port = 3
backlog = 1
size = 1024
s = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
s.bind((hostMACAddress, port))
s.listen(backlog)
#needs to 2 files/needs initial signal for time of simulation

try:
    client, clientInfo = s.accept()
    simulation_time = client.recv(8)
    while 1:
        data = client.recv(size)
        if data:
            print(data)
except: 
    print("Closing socket")
    client.close()
    s.close()
