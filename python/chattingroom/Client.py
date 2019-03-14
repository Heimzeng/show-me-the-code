import socket

BUFFER_SIZE = 1
server_host = '127.0.0.1'
server_port = 4444
client_socket = socket.socket()
client_socket.connect((server_host, server_port))
while True:
    data_to_send = input("Anything: ")
    #data_to_send = "I'm your father."
    #client_socket.send(b"I'm your father.")
    client_socket.send(data_to_send.encode('utf-8'))
client_socket.close()