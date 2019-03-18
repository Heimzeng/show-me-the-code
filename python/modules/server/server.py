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
import math
import random
def loginProcess(rooms):
    BUFFER_SIZE = 1024
    server_socket_tcp = socket.socket()
    server_socket_tcp.bind(('0.0.0.0', 5555))
    server_socket_tcp.listen(3)
    server_socket_tcp.setblocking(0)
    # 注册事件
    epoll = select.epoll()
    epoll.register(server_socket_tcp.fileno(), select.EPOLLIN)
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
        elif room.type == Types.NEWROOM.value:
            pass
        return resRoom.SerializeToString()

    try: 
        while True:
            events = epoll.poll(1)
            for fileno, event in events:
                if fileno == server_socket_tcp.fileno():
                    connection, address = server_socket_tcp.accept()
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
        epoll.unregister(server_socket_tcp.fileno())
        epoll.close()
        server_socket_tcp.close()

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # 使用UDP
server_socket.bind(('0.0.0.0', 5555))
server_socket.setblocking(0)
def gameProcess(rooms, recentaddrs, unackaddrs, alladdrs, unackseq, roomslock):
    # 读写锁，写者优先
    personsroom = dict()
    addrperson = dict()
    BUFFER_SIZE = 1024
    
    epoll = select.epoll()
    epoll.register(server_socket.fileno(), select.EPOLLIN)
    userMgr = user.UserManager()
    def handleData(data, addr=None):
        room = room_pb2.Room()
        room.ParseFromString(data)
        resRoom = room_pb2.Room()
        if room.type == Types.JOINROOM.value:
            person = room.persons[0]
            roomslock.acquire()
            if not rooms[room.id]['person'].get(person.name):
                roomi = rooms[room.id]
                roomi['person'][person.name] = dict()
                roomi['person'][person.name]['addr'] = addr
                roomi['person'][person.name]['action'] = [(0.0, 0)]
                roomi['person'][person.name]['position'] = (0.0, 0.0)
                roomi['person'][person.name]['rotation'] = 0.0
                rooms[room.id] = roomi
                personsroom[person.name] = room.id
                addrperson[addr] = person.name
                print('room ' + str(room.id) + ' add person ' + person.name)
            roomslock.release()
        elif room.type == Types.GAMEDATA.value:
            print('recv seq ' + str(room.seq) + ' len ' + str(len(data)))         
            personname = addrperson[addr]
            roomid = personsroom[personname]
            roomslock.acquire()
            if len(rooms[roomid]['person'][personname]['action']) == room.seq:
                roomi = rooms[roomid]
                roomi['person'][personname]['action'].append((room.rotation, room.direction))
                roomi['person'][personname]['rotation'] = (room.rotation + roomi['person'][personname]['rotation']) % (math.pi * 2)
                roomi['person'][personname]['rotation'] = roomi['person'][personname]['rotation'] * room.direction
                rooms[roomid] = roomi
            else:
                # rooms[roomid]['person'][personname]['action'][room.seq] = (room.rotation, room.direction)
                pass
            roomslock.release()
            roomres = room_pb2.Room()
            roomres.type = Types.ACK.value
            roomres.seq = room.seq
            server_socket.sendto(roomres.SerializeToString(), addr)
            print('send seq ' + str(room.seq) + ' ack to ' + str(addr) )
            
        elif room.type == Types.ACK.value:
            seqs = unackseq[addr]
            for s in seqs:
                if s <= room.seq:
                    seqs.remove(s)
            unackseq[addr] = seqs
            print('recv seq ' + str(room.seq) + ' ack')
            return None
        elif room.type == Types.PING.value:
            if addr in unackaddrs:
                unackaddrs.pop(addr)
        return resRoom.SerializeToString()

    try: 
        while True:
            events = epoll.poll(1)
            for fileno, event in events:
                if fileno == server_socket.fileno():
                    data, addr = server_socket.recvfrom(1024)
                    if not alladdrs.get(addr):
                        alladdrs[addr] = addr
                        print(alladdrs)
                    if not recentaddrs.get(addr):
                        recentaddrs[addr] = 100
                    else:
                        for ad in recentaddrs.keys():
                            if ad == addr:
                                recentaddrs[ad] += 1
                            else:
                                recentaddrs[ad] -= 1
                                if recentaddrs[ad] <= 0:
                                    recentaddrs.pop(ad)
                    response = handleData(data, addr)
                    # server_socket.sendto(response, addr)
    finally:
        print('error')
        epoll.unregister(serversocket.fileno())
        epoll.close()
        serversocket.close()

def heartBeatProcess(recentaddrs, unackaddrs, alladdrs):
    while True:
        for ad in unackaddrs.keys():
            print(str(ad) + ' not ack')
            unackaddrs[ad] -= 1
            if unackaddrs[ad] <= 0:
                # remove conn
                if alladdrs.get(ad):
                    alladdrs.pop(ad)
                if recentaddrs.get(ad):
                    recentaddrs.pop(ad)
                unackaddrs.pop(ad)
        if len(alladdrs) > 0:
            for addr in alladdrs.keys():
                if addr in recentaddrs:
                    continue
                else:
                    room = room_pb2.Room()
                    room.type = Types.PING.value
                    server_socket.sendto(room.SerializeToString(), addr)
                    print('ping ' + str(addr))
                    if not unackaddrs.get(addr):
                        unackaddrs[addr] = 3
            time.sleep(3)

def broadcast(rooms, unackseq, roomid, roomslock):
    # 传入roomid是要为每个room都启动一个线程，不然前面的room会被拖累？
    seq = 0
    while True:
        roomslock.acquire()
        l = rooms[roomid]['person']
        roomslock.release()
        if len(l) > 0:
            flag = True
            # for p in rooms[roomid]['person']:
            #     if len(rooms[roomid]['person'][p]['action']) < seq+1:
            #         flag = False
            if flag:
                roomslock.acquire()
                for p in rooms[roomid]['person']:
                    roomres = room_pb2.Room()
                    roomres.type = Types.GAMEDATA.value
                    roomres.seq = seq + 1
                    seq += 1
                    
                    p1 = roomres.persons.add()
                    data = roomres.SerializeToString()
                    addr = rooms[roomid]['person'][p]['addr']
                    if seq % 10 == 0:
                        keyroom = room_pb2.Room()
                        keyroom.type = Types.KEYROOM.value
                        keyroom.rotation = rooms[roomid]['person'][p]['rotation']
                        server_socket.sendto(keyroom.SerializeToString(), addr)
                    if seq == 1:
                        r = room_pb2.Room()
                        r.type = Types.LOADPACKGE.value
                        p = r.persons.add()
                        for i in range(1000):
                            p.rotation.append(random.random())
                            p.direction.append(random.randint(0, 3))
                        p1 = r.persons.add()
                        for i in range(1000):
                            p1.rotation.append(random.random())
                            p1.direction.append(random.randint(0, 3))
                        d = r.SerializeToString()
                        if len(d) > 1000:
                            pass
                        else:
                            server_socket.sendto(d, addr)
                    server_socket.sendto(data, addr)
                    print('send seq ' + str(seq) + ' to ' + str(addr))
                    if unackseq.get(addr):
                        seqs = unackseq[addr]
                        seqs.append(seq)
                        unackseq[addr] = seqs
                    else:
                        unackseq[addr] = [seq]
                    print(unackseq[addr])
                    for s in unackseq[addr][:10]: # 限制发重前10个，不然发全部会网络拥塞，而且发全部也并没有什么作用
                        if seq - s > 10:
                            roomres = room_pb2.Room()
                            roomres.type = Types.GAMEDATA.value
                            roomres.seq = s
                            p1 = roomres.persons.add()
                            data = roomres.SerializeToString()
                            server_socket.sendto(data, addr)
                            print('resend seq ' + str(s) + ' to ' + str(addr))
                roomslock.release()
                
        time.sleep(0.02)                    
if __name__ == '__main__':
    manager = multiprocessing.Manager()
    rooms = manager.dict()
    rooms[0] = dict()
    room0 = rooms[0]
    room0['person'] = dict()
    rooms[0] = room0
    recentaddrs = manager.dict()
    unackaddrs = manager.dict()
    alladdrs = manager.dict()
    unackseq = manager.dict()
    roomslock = multiprocessing.Lock()
    p = Process(target=loginProcess, args=(rooms, ))
    p.start()
    p2 = Process(target=gameProcess, args=(rooms, recentaddrs, unackaddrs, alladdrs, unackseq, roomslock))
    p2.start()
    p3 = Process(target=heartBeatProcess, args=(recentaddrs, unackaddrs, alladdrs, ))
    p3.start()
    p4 = Process(target=broadcast, args=(rooms, unackseq, 0, roomslock))
    p4.start()
    print('server start!')
    p4.join()
    p.join()
    p2.join()
    p3.join()