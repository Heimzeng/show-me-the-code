import socket
import time
from multiprocessing import Process
import select
import time
import sys
sys.path.append('../')
sys.path.append('../../../')
from serializator.dst import room_pb2
from g.Types import Types


def handleData(data, addr, lastseq, needseq, unackseq, recvseq, client_socket):
    room = room_pb2.Room()
    room.ParseFromString(data)
    if room.type == Types.GAMEDATA.value:
        lastseq = max(lastseq, room.seq)
        if room.seq == needseq:
            print('send seq ' + str(lastseq) + ' ack')
            # render
            room = room_pb2.Room()
            room.type = Types.GAMEDATA.value # ack
            room.seq = needseq
            client_socket.sendto(room.SerializeToString(), addr)                
        else:
            recvseq.append(room.seq)
            print('send seq ' + str(lastseq) + ' ack')
            room = room_pb2.Room()
            room.type = Types.ACK.value # ack
            client_socket.sendto(room.SerializeToString(), addr)
    elif room.type == Types.ACK.value:
        print('recv seq ' + str(room.seq) + ' ack')
        if room.seq in unackseq:
            unackseq.remove(room.seq)
        return None


def clientProcess():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    epoll = select.epoll()
    client_socket.setblocking(0)
    epoll.register(client_socket.fileno(), select.EPOLLIN)
    serveraddr = ('127.0.0.1', 6666)
    lastseq = 0
    needseq = 1
    unackseq = []
    recvseq = []
    t = 0
    flag = Types.LOGIN.value
    username = 'heim'
    password = 'zeng'
    room = room_pb2.Room()
    room.type = flag
    p1 = room.persons.add()
    p1.name = username
    p1.password = password
    data = room.SerializeToString()
    client_socket.sendto(data, serveraddr)
    roomIn = room_pb2.Room()
    roomIn.id = 11
    roomIn.type = Types.JOINROOM.value
    p1 = roomIn.persons.add()
    p1.name = username
    data = roomIn.SerializeToString()
    client_socket.sendto(data, serveraddr)
    seq = 0
    try:
        while True:
            if lastseq == seq:
                t = time.clock()
                roomGame = room_pb2.Room()
                roomGame.type = Types.GAMEDATA.value
                roomGame.seq = seq + 1
                seq += 1
                # roomGame.rotation = random.random() * 360
                # roomGame.direction = int(random.random() * 3)
                data = roomGame.SerializeToString()
                client_socket.sendto(data, serveraddr)
                print('send seq: ' + str(seq) + ' len ' + str(len(data)))
            t = time.clock()
            events = epoll.poll(1)
            for fileno, event in events:
                if fileno == client_socket.fileno():
                    data, addr = client_socket.recvfrom(1024)
                    room = room_pb2.Room()
                    room.ParseFromString(data)
                    if room.type == Types.ACK.value:
                        lastseq = room.seq
                    response = handleData(data, addr, lastseq, needseq, unackseq, recvseq, client_socket)
                    # client_socket.sendto(data, addr)
                    print('ttl: ' + str(time.clock()-t) + ' secends')
    finally:
        print('error')
        epoll.unregister(client_socket.fileno())
        epoll.close()
        client_socket.close()


if __name__ == '__main__':
    cp = Process(target=clientProcess)
    cp.start()
    cp.join()
