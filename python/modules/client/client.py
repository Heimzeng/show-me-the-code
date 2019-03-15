import sys
sys.path.append("../")
from serializator.dst import room_pb2

import socket
import threading

def conn():
    BUFFER_SIZE = 1
    server_host = '127.0.0.1'
    server_port = 4444
    client_socket = socket.socket()
    client_socket.connect((server_host, server_port))
    while True:
        print('please login(0) or regist(1):')
        flag = int(input())
        username = 'heim'
        password = 'zeng'
        if flag == 1:
            password_confirmed = input('Confirm your password: ')
            if password != password_confirmed:
                pass

        room = room_pb2.Room()
        room.id = int(flag) # 0 for login
        p1 = room.persons.add()
        p1.id = 0
        p1.name = username
        p1.password = password
        data = room.SerializeToString()
        client_socket.send(data)

        # while True:
        #     data_to_send = input("Anything: ")
        #     #data_to_send = "I'm your father."
        #     #client_socket.send(b"I'm your father.")
        #     client_socket.send(data_to_send.encode('utf-8'))
    client_socket.close()

if __name__ == '__main__':
    for i in range(1):
        t = threading.Thread(target=conn)
        t.start()
    while True:
        continue