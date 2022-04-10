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

host_ip = '192.168.0.56' 
# connecting to the server
s.connect((host_ip, port))
 
print(f"the socket has successfully connected to {host_ip}")

print('Available commands:')
print('-    Type "exit" to exit this program.')
print('-    Type "send" to send text.')
print('-    Type "receive" to check if there are any messages from the server.')

while True:
    cmd = input("Command: ")
    if cmd == "exit":
        break
    elif cmd == "send":
        text = input("Text to send: ")
        s.send(text.encode())
    elif cmd == "receive":
        data = s.recv(1024)
        if data:
            breakpoint()
            print('Received:', data.decode())
        else:
            print("no data from server")
    else:
        print(f'Invalid command "{cmd}"')

s.close()






