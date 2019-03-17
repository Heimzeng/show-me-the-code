import sys
sys.path.append("../")
from serializator.dst import room_pb2
import select
import socket
import threading
import time
import random
from g.Types import Types
from multiprocessing import Process
BUFFER_SIZE = 1024
server_host = '127.0.0.1'
server_port = 5555
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
lastseq = 0
unackseq = []
def conn():
    global lastseq
    global unackseq
    addr = (server_host, server_port)
    while True:
        # print('please login(0) or regist(1):')
        flag = Types.LOGIN.value
        username = 'heim'
        password = 'zeng'
        # flag = int(input())
        # username = input('username')
        # password = input('password')
        if flag == Types.REGIST.value:
            password_confirmed = input('Confirm your password: ')
            if password != password_confirmed:
                pass
        room = room_pb2.Room()
        room.type = flag
        p1 = room.persons.add()
        p1.name = username
        p1.password = password
        data = room.SerializeToString()
        client_socket.sendto(data, addr)

        roomIn = room_pb2.Room()
        roomIn.id = 11
        roomIn.type = Types.JOINROOM.value
        p1 = roomIn.persons.add()
        p1.name = username
        data = roomIn.SerializeToString()
        client_socket.sendto(data, addr)

        seq = 0
        while True:
            if lastseq >= seq and seq not in unackseq:
            # if True:
                roomGame = room_pb2.Room()
                roomGame.type = Types.GAMEDATA.value
                roomGame.seq = seq + 1
                unackseq.append(seq+1)
                seq += 1
                # roomGame.rotation = random.random() * 360
                # roomGame.direction = int(random.random() * 3)
                data = roomGame.SerializeToString()
                client_socket.sendto(data, addr)
                print('send seq: ' + str(seq) + ' len ' + str(len(data)) + ' to ' + str(addr))
                # time.sleep(0.1)

    client_socket.close()

def recv():
    def handleData(data, addr):
        global lastseq
        global unackseq
        room = room_pb2.Room()
        room.ParseFromString(data)
        if room.type == Types.GAMEDATA.value:
            if len(data) == 2: # is an ack
                print('recv seq ' + str(room.seq) + ' ack')
                if room.seq in unackseq:
                    unackseq.remove(room.seq)
                return None
            lastseq = room.seq
            print('send seq ' + str(lastseq) + ' ack')
            room = room_pb2.Room()
            room.type = Types.GAMEDATA.value # ack
            room.seq = lastseq
            client_socket.sendto(room.SerializeToString(), addr)
    epoll = select.epoll()
    epoll.register(client_socket.fileno(), select.EPOLLIN)
    try: 
        while True:
            events = epoll.poll(1)
            for fileno, event in events:
                if fileno == client_socket.fileno():
                    data, addr = client_socket.recvfrom(1024)
                    if len(data) == 0:
                        print('expty package')
                    response = handleData(data, addr)
    except:
        print('error')
if __name__ == '__main__':
    
    t = threading.Thread(target=conn)
    t.start()
    t2 = threading.Thread(target=recv)
    t2.start()
    while True:
        continue