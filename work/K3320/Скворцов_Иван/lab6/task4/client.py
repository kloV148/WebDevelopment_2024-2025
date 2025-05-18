import socket
import threading

def receive_messages(sock):
    while True:
        try:
            msg = sock.recv(1024).decode()
            print(msg)
        except:
            break

HOST = 'localhost'
PORT = 56789

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

thread = threading.Thread(target=receive_messages, args=(client,))
thread.start()

while True:
    msg = input()
    client.send(msg.encode())