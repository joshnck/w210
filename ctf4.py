import socket

## Host for the MICS CTF and TCP port
host = '128.32.78.55'
port = 8101

## Initiate the socket and perform a TCP handshake for the correct host/port
mySocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
mySocket.connect((host,port))

mySocket.sendall("GET /HTTP/1.1\r\n")
print

## Recieve the first packet to give basic instructions, print to screen
data = mySocket.recv(1024).decode()
print(data)

