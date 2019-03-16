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
import time
def loginProcess():
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

    userMgr = user.UserManager()

    rwl = rwlWriter()

    EOL1 = b'\n\n'
    EOL2 = b'\n\r\n'
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
                    connection, address = server_socket.accept()
                    print("Client addr: ", address)
                    connection.setblocking(0)
                    epoll.register(connection.fileno(), select.EPOLLIN)
                    connections[connection.fileno()] = connection
                    requests[connection.fileno()] = b''
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
        epoll.unregister(serversocket.fileno())
        epoll.close()
        serversocket.close()

def gameProcess():
    def brocast():
        seq = 0
        k = 3
        while True:
            if len(list(rooms[11]['person'])) > 0:
                room = room_pb2.Room()
                room.type = 5
                room.seq = seq
                unackseq.append(seq)
                seq += 1
                server_socket.sendto(room.SerializeToString(), rooms[11]['person']['heim']['addr'])
                print('send seq ' + str(room.seq))
                for s in unackseq:
                    if seq - s > 3:
                        room = room_pb2.Room()
                        room.type = 5
                        room.seq = s
                        server_socket.sendto(room.SerializeToString(), rooms[11]['person']['heim']['addr'])
                        print('resend seq ' + str(s))
                time.sleep(3)
    rooms = dict()
    rooms[11] = dict()
    rooms[11]['person'] = dict()
    unackseq = []
    personsroom = dict()

    BUFFER_SIZE = 50
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    host = '0.0.0.0'
    port = 5555
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
    connections = {}
    requests = {}
    responses = {}

    t = threading.Thread(target=brocast)
    t.start()
    def handleData(data, addr=None):
        room = room_pb2.Room()
        room.ParseFromString(data)

        resRoom = room_pb2.Room()

        if room.type == TYPE_LOGIN:
            person = room.persons[0]
            username = person.name
            password = person.password
            print('user: ' + username + ' try to login!')
            if not userMgr.checkUser({'name':username, 'password':password}):
                resRoom.id = 200
                print('login succ')
                print(userMgr.getAllUsers())
            else:
                resRoom.id = 303
                print('login failed')
        elif room.type == TYPE_REGIST:
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
        elif room.type == 3:
            person = room.persons[0]
            if not rooms[room.id]['person'].get(person.name):
                rooms[room.id]['person'][person.name] = dict()
                rooms[room.id]['person'][person.name]['addr'] = addr
                rooms[room.id]['person'][person.name]['action'] = []
                personsroom[person.name] = room.id
                print('room ' + str(room.id) + ' add person ' + person.name)
        elif room.type == 5:
            person = room.persons[0]
            if len(rooms[room.id]['person'][person.name]['action']) == room.seq:
                rooms[room.id]['person'][person.name]['action'].append((person.rotation, person.direction))
            else:
                rooms[room.id]['person'][person.name]['action'][room.seq] = (person.rotation, person.direction)
            print(rooms[room.id]['person'][person.name]['action'])
            roomres = room_pb2.Room()
            roomres.type = 200
            roomres.seq = room.seq
            server_socket.sendto(roomres.SerializeToString(), addr)
            print('send seq ' + str(room.seq) + ' ack')
        elif room.type == 200:
            if room.seq in unackseq:
                unackseq.remove(room.seq)
                print('recv seq ' + str(room.seq) + ' ack')
        return resRoom.SerializeToString()

    try: 
        while True:
            events = epoll.poll(1)
            for fileno, event in events:
                if fileno == server_socket.fileno():
                    data, addr = server_socket.recvfrom(1024)
                    response = handleData(data, addr)
                    # server_socket.sendto(response, addr)
    finally:
        epoll.unregister(serversocket.fileno())
        epoll.close()
        serversocket.close()

from multiprocessing import Process

if __name__ == '__main__':
    p = Process(target=loginProcess, args=[])
    p.start()
    p2 = Process(target=gameProcess, args=[])
    p2.start()
    p.join()
    p2.join()