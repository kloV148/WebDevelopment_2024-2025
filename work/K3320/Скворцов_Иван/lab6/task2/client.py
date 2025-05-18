import socket

HOST = 'localhost'
PORT = 23456

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    print("Choose operation:")
    print("1 - Pythagorean theorem")
    choice = input("Enter choice: ")

    if choice == '1':
        a = input("Enter a: ")
        b = input("Enter b: ")
        s.sendall(f"{choice} {a} {b}".encode())
        result = s.recv(1024).decode()
        print("Result:", result)