from threading import Thread 
import threading
from Code.PCB import PCB

class Scheduler(Thread):
    def __init__(self, cpu, quantum, readyQueue):
        Thread.__init__(self)
        self.cpu = cpu
        self.quantum = quantum
        self.readyQueue = readyQueue
        self.schedulerAssing = threading.Semaphore(0)
        
    def assignPCB(self):
        print("ejecuto scheduler")
        self.cpu.assignPCB(self.readyQueue.getPcb(),self.quantum)
        
    def run(self):
        while(True):
            self.assignPCB()
            print("asigne un pcb")
            self.schedulerAssing.acquire()
    
    #def startScheduler(self):
        #self.assing.release()        