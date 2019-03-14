import sys
sys.path.append("../")
from protobuf.dst import room_pb2

import socket
import sqlite3

import threading

BUFFER_SIZE = 50
server_socket = socket.socket()
host = '127.0.0.1'
port = 4444
server_socket.bind((host, port))
server_socket.listen(3)

TYPE_LOGIN = 0
TYPE_REGIST = 1

users = dict()

def connectionHandler(client_socket):
    while True:
        bytes_recv = client_socket.recv(BUFFER_SIZE)
        if len(bytes_recv) == 0:
            break
        room = room_pb2.Room()
        room.ParseFromString(bytes_recv)
        if room.id == TYPE_LOGIN:
            person = room.persons[0]
            username = person.name
            password = person.password
            print('user: ' + username + ' try to login!')
            if users.get(username):
                if users[username]['password'] == password:
                    print('password correct')
                else:
                    print('password incorrect')
            else:
                print('user not exists')    
        elif room.id == TYPE_REGIST:
            person = room.persons[0]
            username = person.name
            password = person.password
            if users.get(username):
                print('user exists')
            else:
                users[username] = {'username':username, 'password':password}

while True:
    client_socket, addr = server_socket.accept()
    print("Client addr: ", addr)
    t = threading.Thread(target=connectionHandler, args=(client_socket,))
    t.start()
    # client_socket.close()
    # print('client_socket.close()')