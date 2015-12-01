from threading import Thread
import threading
from Code.IOHandler import IOHandler


class IOManager(Thread):

    def __init__(self,handlerIO):
        Thread.__init__(self)
        self.mutexIO = threading.Semaphore(0)
        self.listIO = []
        self.handlerIO = handlerIO
    
    def run(self):
        self.mutexIO.acquire
        if(self.listIO.__len__() > 0):
            print(self.listIO)
            for irq in self.listIO:
                print("Ejecuto IOManager")
                self.handlerIO.handle(irq)
        self.removeIOFromListIO()
    
    def removeIOFromListIO(self):
        if(self.listIO.__len__() > 0):
            for reqIO in self.listIO:
                self.listIO.remove(reqIO)
              
    def add(self,iOReq):
        self.listIO.append(iOReq)
            
            
