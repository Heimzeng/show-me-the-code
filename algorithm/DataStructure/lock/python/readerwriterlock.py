import threading
import time
class rwlReader:
    def __init__(self): # r for reader, w for writer and f for fair
        self.wLock = threading.Lock()
        self.rcountLock = threading.Lock()
        self.readerCount = 0
    def readAcquire(self):
        self.rcountLock.acquire()
        self.readerCount += 1
        if self.readerCount == 1:
            self.wLock.acquire()
        self.rcountLock.release()
    def readRelease(self):
        self.rcountLock.acquire()
        self.readerCount -= 1
        if self.readerCount == 0:
            self.wLock.release()
        self.rcountLock.release()
    def writeAcquire(self):
        self.wLock.acquire()
    def writeRelease(self):
        self.wLock.release()

class rwlWriter:
    def __init__(self): # r for reader, w for writer and f for fair
        self.rLock = threading.Lock()
        self.wLock = threading.Lock()
        self.rcountLock = threading.Lock()
        self.readerCount = 0
        self.wcountLock = threading.Lock()
        self.writerCount = 0
    def readAcquire(self):
        self.rLock.acquire()
        self.rcountLock.acquire()
        self.readerCount += 1
        if self.readerCount == 1:
            self.wLock.acquire()
        self.rcountLock.release()
        self.rLock.release()
    def readRelease(self):
        self.rcountLock.acquire()
        self.readerCount -= 1
        if self.readerCount == 0:
            self.wLock.release()
        self.rcountLock.release()
    def writeAcquire(self):
        self.wcountLock.acquire()
        self.writerCount += 1
        if self.writerCount == 1:
            self.rLock.acquire()
        self.wcountLock.release()
        self.wLock.acquire()
        
    def writeRelease(self):
        self.wcountLock.acquire()
        self.writerCount -= 1
        if self.writerCount == 0:
            self.rLock.release()
        self.wLock.release()
        self.wcountLock.release()

class rwlFair:
    def __init__(self): 
        self.wLock = threading.Lock()
        self.rcountLock = threading.Lock()
        self.readerCount = 0
        self.fairLock = threading.Lock()
        self.oneSig = threading.Lock()
    def readAcquire(self):
        self.fairLock.acquire()
        self.rcountLock.acquire()
        self.readerCount += 1
        if self.readerCount == 1:
            self.wLock.acquire()
        self.rcountLock.release()
        self.fairLock.release()
    def readRelease(self):
        self.rcountLock.acquire()
        self.readerCount -= 1
        if self.readerCount == 0:
            self.wLock.release()
        self.rcountLock.release()
    def writeAcquire(self):
        self.fairLock.acquire()
        self.wLock.acquire()
        self.fairLock.release()
    def writeRelease(self):
        self.wLock.release()

if __name__ == '__main__':
    def Read(rwl):
        rwl.readAcquire()
        # dosomething
        time.sleep(2)
        print('read')
        rwl.readRelease()
    def Write(rwl):
        rwl.writeAcquire()
        # dosomething
        time.sleep(2)
        print('write')
        rwl.writeRelease()
    def ReaderFirstTest():
        rwl = rwlReader()
        r1 = threading.Thread(target=Read, args=(rwl,))
        r2 = threading.Thread(target=Read, args=(rwl,))
        w1 = threading.Thread(target=Write, args=(rwl,))
        w2 = threading.Thread(target=Write, args=(rwl,))
        w3 = threading.Thread(target=Write, args=(rwl,))
        w3.start()
        r1.start()
        r2.start()
        w1.start()
        w2.start()
    def WriterFirstTest():
        rwl = rwlWriter()
        r1 = threading.Thread(target=Read, args=(rwl,))
        r2 = threading.Thread(target=Read, args=(rwl,))
        w1 = threading.Thread(target=Write, args=(rwl,))
        w2 = threading.Thread(target=Write, args=(rwl,))
        w3 = threading.Thread(target=Write, args=(rwl,))
        r3 = threading.Thread(target=Read, args=(rwl,))
        r4 = threading.Thread(target=Read, args=(rwl,))

        w3.start()
        r1.start()
        r2.start()
        w1.start()
        w2.start()
        r3.start()
        r4.start()
    def FairTest():
        rwl = rwlFair()
        r1 = threading.Thread(target=Read, args=(rwl,))
        r2 = threading.Thread(target=Read, args=(rwl,))
        r3 = threading.Thread(target=Read, args=(rwl,))
        r4 = threading.Thread(target=Read, args=(rwl,))
        w1 = threading.Thread(target=Write, args=(rwl,))
        w2 = threading.Thread(target=Write, args=(rwl,))
        w3 = threading.Thread(target=Write, args=(rwl,))
        
        w3.start()
        r1.start()
        r2.start()
        w1.start()
        w2.start()
        r3.start()
        r4.start()
    # ReaderFirstTest()
    # WriterFirstTest()
    # FairTest()
    pass