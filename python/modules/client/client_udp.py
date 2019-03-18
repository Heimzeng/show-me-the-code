import sys
sys.path.append("../")
sys.path.append('../../../')
from serializator.dst import room_pb2
import select
import socket
import threading
import time
import random
from g.Types import Types
from multiprocessing import Process
import multiprocessing
from algorithm.DataStructure.lock.python.readerwriterlock import rwlWriter
import math
BUFFER_SIZE = 1024
server_host = '172.26.69.155'
server_port = 5555
addr = (server_host, server_port)
addr_tcp = ('172.26.69.155', 5555)
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client_socket.setblocking(0)
client_socket_tcp = socket.socket()
client_socket_tcp.connect(addr_tcp)
# client_socket_tcp.setblocking(0)
lastseq = multiprocessing.Value('i', 0)
manager = multiprocessing.Manager()
unackseq = manager.list()
recvseq = manager.list()
needseq = multiprocessing.Value('i', 1)
t = multiprocessing.Value('f', 0.0)
positoin = multiprocessing.Array('f', [0.0, 0.0, 0.0])
def conn(lastseq, needseq, recvseq, unackseq, t, positoin): 
    while True:
        seq = 0
        k = 10
        while True:
            if needseq.value >= seq - k:# and unackseq[0] >= seq - k: # 不超过10个的丢包或者10个的服务器包延迟
            # 如果是前者，等服务器重传，如果是后者，等关键帧
            # if True:
                roomGame = room_pb2.Room()
                roomGame.type = Types.GAMEDATA.value
                roomGame.seq = seq + 1
                unackseq.append(seq+1)
                seq += 1
                roomGame.rotation = random.random() * math.pi * 2
                roomGame.direction = int(random.random() * 4)
                # 假装自己是个位置计算公式
                positoin[2] = (roomGame.rotation + positoin[2]) % (math.pi * 2)
                positoin[2] = positoin[2] * roomGame.direction

                data = roomGame.SerializeToString()
                client_socket.sendto(data, addr)
                print('send seq: ' + str(seq) + ' len ' + str(len(data)) + ' to ' + str(addr))
                time.sleep(0.02)
    client_socket.close()

def recv(lastseq, needseq, recvseq, unackseq, t, positoin):
    def handleData(data, addr):
        room = room_pb2.Room()
        room.ParseFromString(data)
        if room.type == Types.GAMEDATA.value:
            lastseq.value = max(lastseq.value, room.seq)
            if room.seq == needseq.value:
                print('send seq ' + str(lastseq.value) + ' ack')
                # render
                room = room_pb2.Room()
                room.type = Types.ACK.value # ack
                needseq.value += 1
                # while True:
                #     if needseq.value in recvseq:
                #         recvseq.remove(needseq.value)
                #         # render
                #         # fix position
                #         needseq.value += 1
                #     else:
                #         break
                room.seq = needseq.value - 1
                client_socket.sendto(room.SerializeToString(), addr)                
            else:
                recvseq.append(room.seq)
                print('send seq ' + str(lastseq.value) + ' ack')
                room = room_pb2.Room()
                room.type = Types.ACK.value # ack
                room.seq = needseq.value - 1
                client_socket.sendto(room.SerializeToString(), addr)
        elif room.type == Types.ACK.value:
            print('recv seq ' + str(room.seq) + ' ack')
            for seq in unackseq:
                if seq <= room.seq:
                    unackseq.remove(seq)
            return None
        elif room.type == Types.PING.value:
            room = room_pb2.Room()
            room.type = Types.PING.value
            client_socket.sendto(room.SerializeToString(), addr)
        elif room.type == Types.KEYROOM.value:
            print(abs(room.rotation-positoin[2]) < 0.00001)
    epoll = select.epoll()
    epoll.register(client_socket.fileno(), select.EPOLLIN)
    epoll.register(client_socket_tcp.fileno(), select.EPOLLIN)
    # try: 
    #     while True:
    #         events = epoll.poll(1)
    #         for fileno, event in events:
    #             if fileno == client_socket.fileno():
    #                 data, addr = client_socket.recvfrom(1024)
    #                 response = handleData(data, addr)
    #             if fileno == client_socket_tcp.fileno():
    #                 pass
    # except:
    #     print('error')
    while True:
        events = epoll.poll(1)
        for fileno, event in events:
            if fileno == client_socket.fileno():
                data, addr = client_socket.recvfrom(1024)
                print(len(data))
                response = handleData(data, addr)
if __name__ == '__main__':
    while True:
        flag = int(input('login(0) or regist(1)'))
        username = input('username: ')
        password = input('password(less then 12): ')
        # flag = Types.LOGIN.value
        # username = 'heim'
        # password = 'zeng'
        if flag == Types.REGIST.value:
            password_confirmed = input('Confirm your password: ')
            if password != password_confirmed:
                print('password not the same, restart')
                continue
            elif len(password) > 12:
                print('password too long')
            else:
                break
        break
    room = room_pb2.Room()
    room.type = flag
    p1 = room.persons.add()
    p1.name = username
    p1.password = password
    data = room.SerializeToString()
    client_socket_tcp.send(data)
    # op = input('join room(0) or new room(1)')
    # if (op == '0'):
    #     room = room_pb2.Room()
    #     room.type = Types.GETROOM.value
    #     data = room.SerializeToString()
    #     client_socket_tcp.send(data)
    # elif (op == '1'):
    #     room = room_pb2.Room()
    #     room.type = Types.NEWROOM.value
    #     data = room.SerializeToString()
    #     client_socket_tcp.send(data)
    # join room
    roomIn = room_pb2.Room()
    roomIn.id = 0
    roomIn.type = Types.JOINROOM.value
    p1 = roomIn.persons.add()
    p1.name = username
    data = roomIn.SerializeToString()
    client_socket.sendto(data, addr)
    
    p = Process(target=conn, args=(lastseq, needseq, recvseq, unackseq, t, positoin))
    p2 = Process(target=recv, args=(lastseq, needseq, recvseq, unackseq, t, positoin))
    p.start()
    p2.start()
    p.join()
    p2.join()