from Code.CPU import CPU
from threading import Thread
import time
from ctypes.test.test_errno import threading

class Clock(Thread):

    def __init__(self, cpu, iOManager):
        Thread.__init__(self)
        self.cpu = cpu
        self.iOManager = iOManager

    def run(self):
        while(True):
            self.cpu.mutex.release()
            print("tick a cpu")
            self.iOManager.mutexIO.release()
            print("tick a IO")
            time.sleep(4)
