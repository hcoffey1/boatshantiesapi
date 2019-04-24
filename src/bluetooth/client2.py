import bluetooth

serverMACAddress = 'B8:27:EB:D6:18:99'
port = 3
s = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
s.connect((serverMACAddress, port))
text = 'hello' # Note change to the old (Python 2) raw_input
s.send(text)
s.close()
