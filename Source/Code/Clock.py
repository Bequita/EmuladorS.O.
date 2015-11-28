from Code.CPU import CPU
from threading import Thread
import time

class Clock(Thread):

    def __init__(self, cpu):
        self.CPU = cpu

    def executeClock(self):
        while(True):
            time.sleep(1)
            self.CPU.execute
