import socket
import sqlite3
import multiprocessing

BUFFER_SIZE = 5
server_socket = socket.socket()
host = '127.0.0.1'
port = 4444
server_socket.bind((host, port))
server_socket.listen(3)

while True:
    client_socket, addr = server_socket.accept()
    print("Client addr: ", addr)
    while True:
        bytes_recv = client_socket.recv(BUFFER_SIZE)
        text_recv = bytes_recv.decode('utf-8')
        if text_recv == '':
            break
        print(text_recv)
    client_socket.close()