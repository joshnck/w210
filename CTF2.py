import socket

## Host for the MICS CTF and TCP port
host = '128.32.78.55'
port = 8002

## Initiate the socket and perform a TCP handshake for the correct host/port
mySocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
mySocket.connect((host,port))

## Recieve the first packet to give basic instructions, print to screen
data = mySocket.recv(1024).decode()
print(data)

## This is the first set of math - doesn't change so nothing fancy needs to be done here
message = ""
message += "16\n"
message += "65536\n"
message += "4194304\n"

## Return the packet
mySocket.send(message.encode())

## This bit of instructions from the server are variable - must parse the packet and return the correct data
itr = 0
while(itr < 3):
    data = mySocket.recv(1024).decode()
    print(data)
    message2 = ""

    ## Split the string up so I can parse
    arr = data.splitlines()

    ## Look for the '>' token and then split that string up again and perform the math necessary
    for x in arr:
        if(x.find('>') > -1):
            ## Split it up and [0] = >, [1] = first int, [2] = operator, and [3] = final int
            split = x.split()

            if(len(split) > 3):
                a = int(split[1])
                b = int(split[3])
                c = split[2]
            
                ## I'm looking for different operators. I think we only see + here but...
                if(c == '*'):
                    result = a*b
                elif(c == '+'):
                    result = a+b
                elif(c == '-'):
                    result = a-b
                elif(c == '/'):
                    result = a/b

                itr += 1
                message2 += str(result) + "\n"

    ## send the packet!
    mySocket.send(message2.encode())

## Next challenge includes some even more weird parsing!
## Commenting gets lazy here because this was frustrating and I gave up after it worked

message3 = ""
lst = ""

while(1):
    data = mySocket.recv(1024).decode()
    print(data)

    if(data.startswith('#') == False):
        lst += data.strip('>')
        if(data.endswith('\n')):
            break
    
lst = lst.split()

message3 = int(lst[0])+int(lst[2])
message3 = str(message3) + "\n"
mySocket.send(message3.encode())

while(1):
    data = mySocket.recv(1024).decode()
    print(data)

    data2= data.split()
    print(data2)

    message4 = int(data2[1])+int(data2[3])
    message4 = str(message4) + "\n"
    mySocket.send(message4.encode())    
