__author__ = 'bilge'
from threading import Thread, Semaphore, Lock
import time
import random
mutex = Lock()
index = 0
n=3
buf = []
out_ = 0
in_ = 0
bos = Semaphore(value=n)
dolu = Semaphore(value=0)
class Producer(Thread):

    def run(self):
        global buf
        global in_
        global bos
        global dolu
        while True:
            nums = range(5)
            item = random.choice(nums)
            bos.acquire()
            mutex.acquire()
            buf.append(item)
            in_ = (in_ + 1) % n
            print("P["+str(in_)+"] Producing "+ str(item))
            mutex.release()
            dolu.release()
            time.sleep(random.random())
class Consumer(Thread):
    def run(self):
        global buf
        global out_
        global bos
        global dolu
        while True:
            dolu.acquire()
            mutex.acquire()
            item = buf[out_]
            out_ = (out_ + 1) % n
            print("C["+str(out_)+"] Consuming "+str(item))
            mutex.release()
            bos.release()
            time.sleep(random.random())


Producer().start()
Consumer().start()

