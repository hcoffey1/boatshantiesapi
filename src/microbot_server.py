#!/usr/bin/env python3
import lightblue

sock = lightblue.socket()
try:
    sock.bind(("", 0))    # bind to 0 to bind to a dynamically assigned channel
    lightblue.advertise("OBEX File Transfer", sock, lightblue.OBEX)

    # Receive a file and save it as MyFile.txt.
    # This will wait and block until a file is received.
    print( "Waiting to receive file on channel %d..." % sock.getsockname()[1])
    lightblue.obex.recvfile(sock, "MyFile.txt")

finally:
    sock.close()

print("Saved received file to MyFile.txt!")
