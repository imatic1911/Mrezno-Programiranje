# tcp_server.py
import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
port = 9999
server_socket.bind((host, port))
print("Waiting for connection...")
server_socket.listen(5)

while True:
    conn, addr = server_socket.accept()
    print('Got Connection from', addr)
    conn.send(b'Server Saying Hi')
    conn.close()
