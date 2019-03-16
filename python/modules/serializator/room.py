from dst import room_pb2
import json
import pickle
if __name__ == "__main__":
    room = room_pb2.Room()
    room.id = 11

    p1 = room.persons.add()
    p1.id = 1
    p1.name = 'heim'
    p1.position.append(13.0)
    p1.position.append(14.0)

    data = room.SerializeToString()

    print(len(data))
    print(data)

    roomDict = {
        'id': 11, 
        'persons': {
            'id': 1,
            'name': 'heim',
            'positionx': 13.0,
            'positiony': 13.99999,
        }
    }

    data2 = pickle.dumps(roomDict)
    print(len(data2))
    red = str(1-1.0*len(data)/len(data2))
    print('dict reduce' + red[:4] + '%')

    data3 = json.dumps(roomDict)
    print(len(data3))
    red = str(1-1.0*len(data)/len(data3))
    print('json reduce' + red[:4] + '%')

    room = room_pb2.Room()
    room.id = 11

    p1 = room.persons.add()
    p1.id = 1
    p1.name = 'heim'
    p1.position.append(13.0)
    p1.direction.append(True)
    p1.direction.append(False)

    data_k = room.SerializeToString()
    print('data_k len '+ str(len(data_k)))
    print(data_k)
    roomDict = {
        'id': 11, 
        'persons': {
            'id': 1,
            'name': 'heim',
            'positionx': 13.9999,
            'direction1': True,
            'direction2': False,
        }
    }

    data2 = pickle.dumps(roomDict)
    print(len(data2))
    red = str(1-1.0*len(data_k)/len(data2))
    print('dict reduce' + red[:4] + '%')

    data3 = json.dumps(roomDict)
    print(len(data3))
    red = str(1-1.0*len(data_k)/len(data3))
    print('json reduce' + red[:4] + '%')

    print('2float32->2bool+1float32 reduce:' + str(1-1.0*len(data_k)/len(data)) + '%')