import socket
import sys
import pygame

pygame.init()

pos = 0

screen = pygame.display.set_mode((100, 100))
 
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
    pygame.event.poll()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_d]:
        pos += 1
    if keys[pygame.K_a]:
        pos += 1
    s.send(str(pos).encode())
    data = s.recv(1024)
    if data:
        print(int(data.decode()))
        print(pos)

s.close()






