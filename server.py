import socket

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
                message = input('input: ')
                conn.send(message.encode())
                data = conn.recv(1024)
                if data:
                    print('Received ', data.decode())
                    

except KeyboardInterrupt:
    print('Received Ctrl-C')
except (ConnectionResetError, BrokenPipeError):
    print('Client disconnected.')

print('Exiting server and closing socket')
s.close()
