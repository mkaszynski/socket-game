import socket
import time
import pygame

pygame.init()

screen = pygame.display.set_mode((100, 100))

pos = 0

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
                pygame.event.poll()
                keys = pygame.key.get_pressed()
                if keys[pygame.K_d]:
                    pos += 1
                if keys[pygame.K_a]:
                    pos -= 1
                conn.send(pos.encode())
                data = conn.recv(1024)
                if data:
                    print(data.decode())
                    print(pos)
                time.sleep(0.2)
                    

except KeyboardInterrupt:
    print('Received Ctrl-C')
except (ConnectionResetError, BrokenPipeError):
    print('Client disconnected.')

print('Exiting server and closing socket')
s.close()
