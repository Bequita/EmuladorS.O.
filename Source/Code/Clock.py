import time
from threading import Thread

class Clock(Thread):

    def __init__(self, cpu, iOManager):
        Thread.__init__(self)
        self.cpu = cpu
        self.iOManager = iOManager

    def run(self):
        while(True):
            self.cpu.mutex.notify()
            print("tick a cpu")
            self.iOManager.mutexIO.notify()
            print("tick a IO")
            time.sleep(4)
