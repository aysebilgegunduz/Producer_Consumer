__author__ = 'bilge'
from threading import Thread, Semaphore, Lock
mutex = Lock()

class uretici_tuketici():
    def __init__(self,n):
        self.buf = []
        self.out_ = 0
        self.in_ = 0
        self.bos = Semaphore(value=n)
        self.dolu = Semaphore(value=0)

    def Producer(self, n, veri):
        for i in (0,n):
            item = i
            self.bos.acquire()
            mutex.acquire()
            self.buf.append(item)
            self.in_ = (self.in_ + 1) % n
            print("P["+str(i)+"] Producing "+ str(item))
            mutex.release()
            self.dolu.release()
    def Consumer(self,n):
        for i in (0,n):
            self.dolu.acquire()
            mutex.acquire()
            item = self.buf[self.bos]
            self.out_ = (self.out_ + 1) % n
            print("C["+str(i)+"] Consuming "+str(item))
            mutex.release()
            self.bos.release()

idP = Thread()
idC = Thread()
index = 0
prod_cons = uretici_tuketici(3)
for i in (0,3):
    idP = Thread(target=prod_cons.Producer(3,i), args=3)
    idP.start()
for i in (0,3):
    idC = Thread(target=prod_cons.Consumer(3), args=3)
    idC.start()
