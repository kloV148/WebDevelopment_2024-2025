import socket
import threading

clients = []

def broadcast(message, conn):
    for client in clients:
        if client != conn:
            try:
                client.send(message)
            except:
                client.close()
                clients.remove(client)

def handle_client(conn, addr):
    print(f"New connection from {addr}")
    clients.append(conn)
    while True:
        try:
            msg = conn.recv(1024)
            if not msg:
                break
            broadcast(msg, conn)
        except:
            clients.remove(conn)
            conn.close()
            break

HOST = 'localhost'
PORT = 56789

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()
print("Chat server started...")

while True:
    conn, addr = server.accept()
    thread = threading.Thread(target=handle_client, args=(conn, addr))
    thread.start()