import socket
import sys
import pygame
import time
import ast

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
    screen.fill((255, 255, 255))
    pygame.event.poll()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_d]:
        pos[0] += 5
    if keys[pygame.K_a]:
        pos[0] -= 5
    if keys[pygame.K_w]:
        pos[1] -= 5
    if keys[pygame.K_s]:
        pos[1] += 5
    s.send(str(pos).encode())
    data = s.recv(1024)
    # if data:
    data = data.decode()
    map1 = pygame.Rect(ast.literal_eval(data)[0] - pos[0], ast.literal_eval(data)[1] - pos[1], 20, 20)
    pygame.draw.rect(screen, (0, 0, 0), map1)
    map1 = pygame.Rect(600, 300, 20, 20)
    pygame.draw.rect(screen, (0, 0, 0), map1)
    
    time.sleep(1/60)
    
    pygame.display.flip()

s.close()






