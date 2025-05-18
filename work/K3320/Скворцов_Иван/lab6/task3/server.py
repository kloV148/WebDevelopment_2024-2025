import socket

HOST = 'localhost'
PORT = 8080

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen(1)
    print('HTTP Server running...')
    conn, addr = s.accept()
    with conn:
        request = conn.recv(1024)
        print('Request received:')
        print(request.decode())

        with open("index.html", "r") as f:
            response_body = f.read()

        response = 'HTTP/1.1 200 OK\r\n'
        response += 'Content-Type: text/html\r\n\r\n'
        response += response_body

        conn.sendall(response.encode())