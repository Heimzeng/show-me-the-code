from dst import room_pb2
if __name__ == "__main__":
    room = room_pb2.Room()
    room.id = 11

    p1 = room.persons.add()
    p1.id = 1
    p1.name = 'heim'
    p2 = room.persons.add()
    p2.id = 3
    p2.name = 'h'

    data = room.SerializeToString()

    print(len(data))
    print(data)

    room2 = room_pb2.Room()
    room2.ParseFromString(data)

    print(room2)