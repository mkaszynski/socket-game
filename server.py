import socket
import time
import pygame
import ast

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
                    pos[0] += 5
                if keys[pygame.K_a]:
                    pos[0] -= 5
                if keys[pygame.K_w]:
                    pos[1] -= 5
                if keys[pygame.K_s]:
                    pos[1] += 5
                conn.send(str(pos).encode())
                data = conn.recv(1024).decode()
                # if data:
                map1 = pygame.Rect(ast.literal_eval(data)[0], ast.literal_eval(data)[1], 20, 20)
                pygame.draw.rect(screen, (0, 0, 0), map1)
                map1 = pygame.Rect(pos[0], pos[1], 20, 20)
                pygame.draw.rect(screen, (0, 0, 0), map1)
                
                time.sleep(1/60)
                
                pygame.display.flip()
                    

except KeyboardInterrupt:
    print('Received Ctrl-C')
except (ConnectionResetError, BrokenPipeError):
    print('Client disconnected.')
except Exception as e:
    print(f'unhandled exception {str(e)}')

print('Exiting server and closing socket')
s.close()
