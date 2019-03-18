import multiprocessing as mp
from multiprocessing import Process, Manager
def add(d):
    for i in range(100):
        d[0] += 1
if __name__ == '__main__':
    m = Manager()
    d = m.dict()
    d[0] = 0
    for i in range(10):
        p = Process(target=add, args=(d, ))
        p.start()
    p = Process(target=add, args=(d, ))
    p.start()
    p.join()
    print(d[0])