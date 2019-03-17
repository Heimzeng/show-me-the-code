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
from g.Types import Types
from multiprocessing import Process
import multiprocessing
def loginProcess():
    BUFFER_SIZE = 1024
    server_socket = socket.socket()
    server_socket.bind(('0.0.0.0', 4444))
    server_socket.listen(3)
    server_socket.setblocking(0)
    # 注册事件
    epoll = select.epoll()
    epoll.register(server_socket.fileno(), select.EPOLLIN)
    # 用户管理模块
    userMgr = user.UserManager()
    # 读写锁，写者优先
    rwl = rwlWriter()

    connections = {}    # 储存所有TCP连接
    requests = {}   # 储存所有request的bytes
    responses = {}  # 储存所有要response的bytes

    def handleData(data):
        room = room_pb2.Room()
        room.ParseFromString(data)
        resRoom = room_pb2.Room()
        if room.type == Types.LOGIN.value:
            person = room.persons[0]
            username = person.name
            password = person.password
            if not userMgr.checkUser({'name':username, 'password':password}):
                resRoom.type = Types.SUCC.value
                print('user: ' + username + ' login!')
            else:
                resRoom.type = Types.FAILED.value
                print('user: ' + username + ' login failed')
        elif room.type == Types.REGIST.value:
            person = room.persons[0]
            username = person.name
            password = person.password
            if not userMgr.addUser({'name':username, 'password':password}):
                resRoom.type = Types.SUCC.value
            else:
                resRoom.type = Types.FAILED.value
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
        seq = 1
        k = 10
        time.sleep(5)
        while True:
            if len(list(rooms[11]['person']['heim']['action'])) > 0:
                room = room_pb2.Room()
                room.type = Types.GAMEDATA.value
                room.seq = seq
                p1 = room.persons.add()
                p2 = room.persons.add()
                unackseq.append(seq)
                seq += 1
                data = room.SerializeToString()
                server_socket.sendto(data, rooms[11]['person']['heim']['addr'])
                print('send seq ' + str(room.seq) + ' len ' + str(len(data)))
                # resend unack packet 
                # for s in unackseq:
                #     if seq - s > k:
                #         room = room_pb2.Room()
                #         room.type = Types.GAMEDATA.value
                #         room.seq = s
                #         server_socket.sendto(room.SerializeToString(), rooms[11]['person']['heim']['addr'])
                #         print('resend seq ' + str(s))
                time.sleep(0.2)
    rooms = dict()
    rooms[11] = dict()
    rooms[11]['person'] = dict()
    unackseq = []
    personsroom = dict()
    addrperson = dict()

    BUFFER_SIZE = 1024
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # 使用UDP
    server_socket.bind(('0.0.0.0', 5555))
    server_socket.setblocking(0)

    epoll = select.epoll()
    epoll.register(server_socket.fileno(), select.EPOLLIN)

    userMgr = user.UserManager()
    rwl = rwlWriter()

    connections = {}
    requests = {}
    responses = {}

    t = threading.Thread(target=brocast)
    t.start()
    # change to process to improve the speed
    # pp = multiprocessing.Pipe()
    # pp2 = multiprocessing.Pipe()
    # p = Process(target=brocast, args=(server_socket, pp[1], pp2[1]))
    # p.start()
    def handleData(data, addr=None):
        room = room_pb2.Room()
        room.ParseFromString(data)

        resRoom = room_pb2.Room()

        if room.type == Types.LOGIN.value:
            person = room.persons[0]
            username = person.name
            password = person.password
            print('user: ' + username + ' try to login!')
            if not userMgr.checkUser({'name':username, 'password':password}):
                resRoom.type = Types.SUCC.value
                print('login succ')
            else:
                resRoom.type = Types.FAILED.value
                print('login failed')
        elif room.type == Types.REGIST.value:
            person = room.persons[0]
            username = person.name
            password = person.password
            if not userMgr.addUser({'name':username, 'password':password}):
                resRoom.type = Types.SUCC.value
            else:
                resRoom.type = Types.FAILED.value
        elif room.type == Types.JOINROOM.value:
            person = room.persons[0]
            if not rooms[room.id]['person'].get(person.name):
                rooms[room.id]['person'][person.name] = dict()
                rooms[room.id]['person'][person.name]['addr'] = addr
                rooms[room.id]['person'][person.name]['action'] = [(0.0, 0)]
                personsroom[person.name] = room.id
                addrperson[addr] = person.name
                print('room ' + str(room.id) + ' add person ' + person.name)
                
        elif room.type == Types.GAMEDATA.value:
            if len(data) == 2: # is an ack
                if room.seq in unackseq:
                    unackseq.remove(room.seq)
                    print('recv seq ' + str(room.seq) + ' ack')
                    return None
            print('recv seq ' + str(room.seq) + ' len ' + str(len(data)))            
            personname = addrperson[addr]
            roomid = personsroom[personname]
            if len(rooms[roomid]['person'][personname]['action']) == room.seq:
                rooms[roomid]['person'][personname]['action'].append((room.rotation, room.direction))
            else:
                # rooms[roomid]['person'][personname]['action'][room.seq] = (room.rotation, room.direction)
                pass
            # print(rooms[room.id]['person'][person.name]['action'])
            roomres = room_pb2.Room()
            roomres.type = Types.GAMEDATA.value
            roomres.seq = room.seq
            server_socket.sendto(roomres.SerializeToString(), addr)
            print('send seq ' + str(room.seq) + ' ack')
        return resRoom.SerializeToString()

    try: 
        while True:
            events = epoll.poll(1)
            for fileno, event in events:
                if fileno == server_socket.fileno():
                    data, addr = server_socket.recvfrom(1024)
                    if len(data) == 0:
                        print('empty data')
                    response = handleData(data, addr)
                    # server_socket.sendto(response, addr)
    finally:
        epoll.unregister(serversocket.fileno())
        epoll.close()
        serversocket.close()



if __name__ == '__main__':
    p = Process(target=loginProcess, args=[])
    p.start()
    p2 = Process(target=gameProcess, args=[])
    p2.start()
    p.join()
    p2.join()