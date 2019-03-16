import sys
sys.path.append('../')
sys.path.append('../../../')
from serializator.dst import room_pb2

import socket
import sqlite3

import threading

from algorithm.DataStructure.lock.python.readerwriterlock import rwlWriter

import select

from user import user

BUFFER_SIZE = 50
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
host = '0.0.0.0'
port = 4444
server_socket.bind((host, port))
server_socket.setblocking(0)

epoll = select.epoll()
epoll.register(server_socket.fileno(), select.EPOLLIN)

TYPE_LOGIN = 0
TYPE_REGIST = 1

users = dict()

userMgr = user.UserManager()

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
        # rwl.readAcquire()
        # if users.get(username):
        #     if users[username]['password'] == password:
        #         print('password correct')
        #         resRoom.id = 200
        #     else:
        #         print('password incorrect')
        #         resRoom.id = 303
        # else:
        #     print('user not exists')
        #     resRoom.id = 404
        # rwl.readRelease()

        if not userMgr.checkUser({'name':username, 'password':password}):
            resRoom.id = 200
            print('login succ')
            print(userMgr.getAllUsers())
        else:
            resRoom.id = 303
            print('login failed')
    elif room.id == TYPE_REGIST:
        person = room.persons[0]
        username = person.name
        password = person.password
        # dict version
        # rwl.readAcquire()
        # if users.get(username):
        #     print('user exists')
        #     resRoom.id = 404
        # else:
        #     rwl.readRelease()
        #     rwl.writeAcquire()
        #     users[username] = {'username': username, 'password': password}
        #     rwl.writeRelease()
        #     resRoom.id = 200

        # sql version
        if not userMgr.addUser({'name':username, 'password':password}):
            resRoom.id = 200
        else:
            print('user exists')
            resRoom.id = 404
    return resRoom.SerializeToString()

try: 
    while True:
        events = epoll.poll(1)
        for fileno, event in events:
            if fileno == server_socket.fileno():
                data, addr = server_socket.recvfrom(1024)
                response = handleData(data)
                server_socket.sendto(data, addr)
finally:
    epoll.unregister(serversocket.fileno())
    epoll.close()
    serversocket.close()