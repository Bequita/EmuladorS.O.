import time
from threading import Thread

class Clock(Thread):

    def __init__(self,systemComponents):
        Thread.__init__(self)
        self.cpu = systemComponents.cpu
        self.iOManager = systemComponents.iOManager
        self.memory = systemComponents.mem

    def run(self):
        while(True):
            with self.cpu.mutex:
                print("tick a cpu")
                self.cpu.mutex.notify()
            with self.iOManager.mutexIO:
                print("tick a IO")
                self.iOManager.mutexIO.notify()
                time.sleep(4)
            print(self.memory.blocksTable)
            #print(mem.blockSize)
            #print(self.memory.firstBlockFree())
            #print(mem.hardDisk)
            #print(mem.memoryBlocks)
            #print(self.memory.spaceFreeInMemory())
