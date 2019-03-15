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
host = '0.0.0.0'
port = 4444
server_socket.bind((host, port))
server_socket.listen(3)
# server_socket.setblocking(0)

TYPE_LOGIN = 0
TYPE_REGIST = 1


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

while True:
    client_socket, addr = server_socket.accept()
    print("Client addr: ", addr)
    t = threading.Thread(target=connectionHandler, args=(client_socket,))
    conn = Conn(client_socket, t)
    conns.append(conn)
    t.start()
    # client_socket.close()
    # print('client_socket.close()')