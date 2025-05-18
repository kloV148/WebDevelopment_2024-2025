import socket

HOST = 'localhost'
PORT = 4321

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    print('Server is listening...')
    conn, addr = s.accept()
    with conn:
        print('Connected by', addr)
        data = conn.recv(1024)
        print('Received from client:', data.decode())
        conn.sendall(b'Hello, client')