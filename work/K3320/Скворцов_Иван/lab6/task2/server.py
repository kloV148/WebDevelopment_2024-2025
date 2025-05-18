import socket
import math

HOST = 'localhost'
PORT = 23456

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    print('Server listening for math operations...')
    conn, addr = s.accept()
    with conn:
        print('Connected by', addr)
        data = conn.recv(1024).decode().split()
        choice, a, b = data
        if choice == '1':
            result = math.sqrt(float(a)**2 + float(b)**2)
        conn.sendall(str(result).encode())