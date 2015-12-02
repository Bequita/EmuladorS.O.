from threading import Thread 
import threading
from Code.PCB import PCB

class Scheduler(object):
    def __init__(self, sistemComponents):
        self.cpu = sistemComponents.cpu
        self.quantum = sistemComponents.quantum
        self.readyQueue = sistemComponents.readyQueue
        self.schedulerAssing = threading.Semaphore(0)
        
    def assignPCB(self):
        print("ejecuto scheduler")
        self.cpu.assignPCB(self.readyQueue.getPcb(),self.quantum)
        
    def addPCB(self,pcb):
        self.readyQueue.addPcb(pcb)