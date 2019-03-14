import sys
sys.path.append("../")
sys.path.append("../../../")
from serializator.dst import room_pb2

import socket
import sqlite3

import threading

from algorithm.DataStructure.lock.python.readerwriterlock import rwlWriter

import select

BUFFER_SIZE = 50
server_socket = socket.socket()
host = '127.0.0.1'
port = 4444
server_socket.bind((host, port))
server_socket.listen(3)
server_socket.setblocking(0)

epoll = select.epoll()
epoll.register(server_socket.fileno(), select.EPOLLIN)

TYPE_LOGIN = 0
TYPE_REGIST = 1

# class ConnectionHandler

class Conn:
    def __init__(self, socket=None, thread=None):
        self.socket = socket
        self.thread = thread

users = dict()
rwl = rwlWriter()
conns = []         

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
            rwl.readAcquire()
            if users.get(username):
                if users[username]['password'] == password:
                    print('password correct')
                else:
                    print('password incorrect')
            else:
                print('user not exists')
            rwl.readRelease()   
        elif room.id == TYPE_REGIST:
            person = room.persons[0]
            username = person.name
            password = person.password
            rwl.readAcquire()
            if users.get(username):
                print('user exists')
            else:
                rwl.readRelease()
                rwl.writeAcquire()
                users[username] = {'username':username, 'password':password}
                rwl.writeRelease()

EOL1 = b'\n\n'
EOL2 = b'\n\r\n'
connections = {}; requests = {}; responses = {}
while True:
    # multithreading version
    # client_socket, addr = server_socket.accept()
    # print("Client addr: ", addr)
    # t = threading.Thread(target=connectionHandler, args=(client_socket,))
    # conn = Conn(client_socket, t)
    # conns.append(conn)
    # t.start()
    # client_socket.close()
    # print('client_socket.close()')

    # epoll version
    events = epoll.poll(1)
    for fileno, event in events:
        if fileno == server_socket.fileno():
            connection, address = server_socket.accept()
            connection.setblocking(0)
            epoll.register(connection.fileno(), select.EPOLLIN)
            connections[connection.fileno()] = connection
            requests[connection.fileno()] = b''
            responses[connection.fileno()] = b'Helloworld!'
        elif event & select.EPOLLIN:
            requests[fileno] += connections[fileno].recv(1024)
            if EOL1 in requests[fileno] or EOL2 in requests[fileno]:
                epoll.modify(fileno, select.EPOLLOUT)
        elif event & select.EPOLLOUT:
            byteswritten = connections[fileno].send(responses[fileno])
            responses[fileno] = responses[fileno][byteswritten:]
            if len(responses[fileno]) == 0:
                epoll.modify(fileno, 0)
                connections[fileno].shutdown(socket.SHUT_RDWR)
        elif event & select.EPOLLHUP:
            epoll.unregister(fileno)
            connections[fileno].close()
            del connections[fileno]