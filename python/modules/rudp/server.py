import socket
from multiprocessing import Process
import select
import sys
sys.path.append('../')
sys.path.append('../../../')
from g.Types import Types
from serializator.dst import room_pb2
from user import user

def handleData(data, addr, userMgr, rooms, server_socket, unackseq, personsroom, addrperson):
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
        roomres.type = Types.ACK.value
        roomres.seq = room.seq
        server_socket.sendto(roomres.SerializeToString(), addr)
        print('send seq ' + str(room.seq) + ' ack to ' + str(addr) )
        # to delete
        roomres = room_pb2.Room()
        roomres.type = Types.GAMEDATA.value
        roomres.seq = room.seq
        p1 = roomres.persons.add()
        data = roomres.SerializeToString()
        server_socket.sendto(data, addr)
        print('send seq ' + str(roomres.seq) + ' len ' + str(len(data)))
    elif room.type == Types.ACK.value:
        for s in unackseq:
            if s <= room.seq:
                unackseq.remove(s)
        print('recv seq ' + str(room.seq) + ' ack')
        return None
    return resRoom.SerializeToString()
def gameProcess():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind(('0.0.0.0', 6666))
    server_socket.setblocking(0)
    epoll = select.epoll()
    epoll.register(server_socket.fileno(), select.EPOLLIN)
    rooms = dict()
    rooms[11] = dict()
    rooms[11]['person'] = dict()
    unackseq = []
    personsroom = dict()
    addrperson = dict()
    userMgr = user.UserManager()
    try: 
        while True:
            events = epoll.poll(1)
            for fileno, event in events:
                if fileno == server_socket.fileno():
                    data, addr = server_socket.recvfrom(1024)
                    response = handleData(data, addr, userMgr, rooms, server_socket, unackseq, personsroom, addrperson)
                    server_socket.sendto(data, addr)
    finally:
        print('error')
        epoll.unregister(server_socket.fileno())
        epoll.close()
        server_socket.close()
if __name__ == '__main__':
    gp = Process(target=gameProcess)
    gp.start()
    gp.join()