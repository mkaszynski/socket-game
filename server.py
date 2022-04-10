import socket
import time
import pygame

pygame.init()

screen = pygame.display.set_mode([1200, 600])

pos = [0, 0]

HOST = "0.0.0.0"  # Standard loopback interface address (localhost)
PORT = 60001  # Port to listen on (non-privileged ports are > 1023)

try:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        print(f"Server started at {HOST}:{PORT}")
        s.bind((HOST, PORT))
        s.listen()
        conn, addr = s.accept()
        with conn:
            print(f"Connection opened at {addr}")
            while True:
                screen.fill((255, 255, 255))
                pygame.event.poll()
                keys = pygame.key.get_pressed()
                if keys[pygame.K_d]:
                    pos[0] += 1
                if keys[pygame.K_a]:
                    pos[0] -= 1
                if keys[pygame.K_d]:
                    pos[1] -= 1
                if keys[pygame.K_a]:
                    pos[1] += 1
                conn.send(bytes(pos))
                data = conn.recv(1024)
                if data:
                    map1 = pygame.Rect(list(data)[0], list(data)[1], 20, 20)
                    pygame.draw.rect(screen, (255, 255, 255), map1)
                    map1 = pygame.Rect(pos[0], pos[1], 20, 20)
                    pygame.draw.rect(screen, (255, 255, 255), map1)
                time.sleep(1/60)
                    

except KeyboardInterrupt:
    print('Received Ctrl-C')
except (ConnectionResetError, BrokenPipeError):
    print('Client disconnected.')

print('Exiting server and closing socket')
s.close()
