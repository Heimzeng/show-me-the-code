import sys
sys.path.append("../")
from serializator.dst import room_pb2

import socket
import threading
import time
import random

BUFFER_SIZE = 1
server_host = '127.0.0.1'
server_port = 5555
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
lastseq = -1
unackseq = []
def conn():
    global lastseq
    global unackseq
    addr = (server_host, server_port)
    while True:
        # print('please login(0) or regist(1):')
        flag = 0
        username = 'heim'
        password = 'zeng'
        # flag = int(input())
        # username = input('username')
        # password = input('password')
        if flag == 1:
            password_confirmed = input('Confirm your password: ')
            if password != password_confirmed:
                pass
        room = room_pb2.Room()
        room.type = int(flag) # 0 for login
        p1 = room.persons.add()
        p1.id = 0
        p1.name = username
        p1.password = password
        data = room.SerializeToString()
        client_socket.sendto(data, addr)

        roomIn = room_pb2.Room()
        roomIn.id = 11
        roomIn.type = 3
        p1 = roomIn.persons.add()
        p1.id = 0
        p1.name = username
        data = roomIn.SerializeToString()
        client_socket.sendto(data, addr)

        seq = -1
        while True:
            if lastseq >= seq and seq not in unackseq:
                roomGame = room_pb2.Room()
                roomGame.id = 11
                roomGame.type = 5
                roomGame.seq = seq + 1
                unackseq.append(seq+1)
                seq = roomGame.seq
                p1 = roomGame.persons.add()
                p1.id = 0
                p1.name = username
                p1.rotation = random.random() * 360
                p1.direction = int(random.random() * 3)
                data = roomGame.SerializeToString()
                client_socket.sendto(data, addr)
                print('send seq: ' + str(seq))

    client_socket.close()

def recv():
    global lastseq
    global unackseq
    while True:
        data, addr = client_socket.recvfrom(1024)
        if len(data) == 0:
            continue
        room = room_pb2.Room()
        room.ParseFromString(data)
        if room.type == 5:
            lastseq = room.seq
            print('send seq ' + str(lastseq) + ' ack')
            room = room_pb2.Room()
            room.type = 200 # ack
            room.seq = lastseq
            client_socket.sendto(room.SerializeToString(), addr)
        elif room.type == 200:
            print('recv seq ' + str(room.seq) + ' ack')
            if room.seq in unackseq:
                unackseq.remove(room.seq)
if __name__ == '__main__':
    for i in range(1):
        t = threading.Thread(target=conn)
        t.start()
    t2 = threading.Thread(target=recv)
    t2.start()

    while True:
        continue