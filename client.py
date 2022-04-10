import socket
import sys
import pygame
import time

pygame.init()

pos = [0, 0]

screen = pygame.display.set_mode([1200, 600])
 
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print ("Socket successfully created")
except socket.error as err:
    print ("socket creation failed with error %s" %(err))
 
# default port for socket
port = 60001

host_ip = '192.168.0.149' 
# connecting to the server
try:
    s.connect((host_ip, port))
except:
    print(f'host {host_ip} is not running')
    sys.exit()
 
print(f"the socket has successfully connected to {host_ip}")


while True:
    pygame.event.poll()
    keys = pygame.key.get_pressed()
    screen.fill((255, 255, 255))
    if keys[pygame.K_d]:
        pos[0] += 1
    if keys[pygame.K_a]:
        pos[0] -= 1
    if keys[pygame.K_d]:
        pos[1] -= 1
    if keys[pygame.K_a]:
        pos[1] += 1
    s.send(pos)
    data = s.recv(1024)
    if data:
        map1 = pygame.Rect(data[0], data[1], 20, 20)
        pygame.draw.rect(screen, (0, 0, 0), map1)
        map1 = pygame.Rect(pos[0], pos[1], 20, 20)
        pygame.draw.rect(screen, (0, 0, 0), map1)
    time.sleep(1/60)

s.close()






