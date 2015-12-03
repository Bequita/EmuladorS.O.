import time
from threading import Thread

class Clock(Thread):

    def __init__(self,systemComponents):
        Thread.__init__(self)
        self.cpu = systemComponents.cpu
        self.iOManager = systemComponents.iOManager

    def run(self):
        while(True):
            self.cpu.mutex.notify()
            print("tick a cpu")
            self.iOManager.mutexIO.notify()
            print("tick a IO")
            time.sleep(4)
