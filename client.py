"""Demo socket communication

client

"""

import socket
import sys
 
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print ("Socket successfully created")
except socket.error as err:
    print ("socket creation failed with error %s" %(err))
 
# default port for socket
port = 60001

host_ip = '192.168.0.149' 
# connecting to the server
s.connect((host_ip, port))
 
print(f"the socket has successfully connected to {host_ip}")


while True:
    data = s.recv(1024)
    if data:
        print('Received: ', data.decode())
    else:
        message = input("input: ")
        if message == "exit":
            break
        s.send(message.encode())

s.close()






