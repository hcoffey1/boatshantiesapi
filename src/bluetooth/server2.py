import bluetooth

hostMACAddress = 'B0:10:41:77:51:10' # The MAC address of a Bluetooth adapter on the server. The server might have multiple Bluetooth adapters.
port = 3000
backlog = 1
size = 1024
s = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
s.bind((hostMACAddress, port))
s.listen(backlog)
#needs to 2 files/needs initial signal for time of simulation

try:
    client, clientInfo = s.accept()
    data = client.recv(size)
    print(data)
except:
    print("Closing socket")
    client.close()
    s.close()
