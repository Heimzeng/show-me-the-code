from enum import Enum

class Types(Enum):
    GAMEDATA = 0
    LOGIN = 1
    REGIST = 2
    NEWROOM = 3
    JOINROOM = 4
    READY = 5
    STARTGAME = 6
    REALLYSTART = 7
    ACK = 8

    GETROOM = 9
    KEYROOM = 10
    LOADPACKGE = 11
    PING = 99

    SUCC = 200
    FAILED = 400
    NOTFOUND = 404