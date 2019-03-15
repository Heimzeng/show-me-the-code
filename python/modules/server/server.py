import sys
sys.path.append('../')
sys.path.append('../../../')
from serializator.dst import room_pb2

import socket
import sqlite3

import threading

from algorithm.DataStructure.lock.python.readerwriterlock import rwlWriter

import select

BUFFER_SIZE = 50
server_socket = socket.socket()
host = '0.0.0.0'
port = 4444
server_socket.bind((host, port))
server_socket.listen(3)
server_socket.setblocking(0)

epoll = select.epoll()
epoll.register(server_socket.fileno(), select.EPOLLIN)

TYPE_LOGIN = 0
TYPE_REGIST = 1

users = dict()
rwl = rwlWriter()

EOL1 = b'\n\n'
EOL2 = b'\n\r\n'
response = b'HTTP/1.0 200 OK\r\nDate: Mon, 1 Jan 1996 01:01:01 GMT\r\n'
response += b'Content-Type: text/plain\r\nContent-Length: 13\r\n\r\n'
response += b'Hello, world!'
connections = {}
requests = {}
responses = {}


def handleData(data):
    room = room_pb2.Room()
    room.ParseFromString(data)

    resRoom = room_pb2.Room()

    if room.id == TYPE_LOGIN:
        person = room.persons[0]
        username = person.name
        password = person.password
        print('user: ' + username + ' try to login!')
        rwl.readAcquire()
        if users.get(username):
            if users[username]['password'] == password:
                print('password correct')
                resRoom.id = 200
            else:
                print('password incorrect')
                resRoom.id = 303
        else:
            print('user not exists')
            resRoom.id = 404
        rwl.readRelease()
    elif room.id == TYPE_REGIST:
        person = room.persons[0]
        username = person.name
        password = person.password
        rwl.readAcquire()
        if users.get(username):
            print('user exists')
            resRoom.id = 404
        else:
            rwl.readRelease()
            rwl.writeAcquire()
            users[username] = {'username': username, 'password': password}
            rwl.writeRelease()
            resRoom.id = 200
    return resRoom.SerializeToString()

try: 
    while True:
        events = epoll.poll(1)
        for fileno, event in events:
            if fileno == server_socket.fileno():
                connection, address = server_socket.accept()
                print("Client addr: ", address)
                connection.setblocking(0)
                epoll.register(connection.fileno(), select.EPOLLIN)
                connections[connection.fileno()] = connection
                requests[connection.fileno()] = b''
                responses[connection.fileno()] = response
            elif event & select.EPOLLIN:
                requests[fileno] += connections[fileno].recv(1024)
                # if EOL1 in requests[fileno] or EOL2 in requests[fileno]:
                # generate response
                responses[fileno] = handleData(requests[fileno])
                requests[fileno] = b''
                epoll.modify(fileno, select.EPOLLOUT)
            elif event & select.EPOLLOUT:
                byteswritten = connections[fileno].send(responses[fileno])
                responses[fileno] = responses[fileno][byteswritten:]
                if len(responses[fileno]) == 0:
                    epoll.modify(fileno, select.EPOLLIN)
                    # connections[fileno].shutdown(socket.SHUT_RDWR)
            elif event & select.EPOLLHUP:
                epoll.unregister(fileno)
                connections[fileno].close()
                del connections[fileno]
finally:
    pass