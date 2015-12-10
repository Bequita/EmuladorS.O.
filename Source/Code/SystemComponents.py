from Code.HardDisk import HardDisk
from Code.Memory import Memory
from Code.ReadyQueue import ReadyQueue
from Code.InterruptionManager import InterruptionManager
from Code.TimeOutHandler import TimeOutHandler

class SystemComponents(object):

    def __init__(self):#(self,kernel,cpu,hd,mem,readyQueue,iOManager,InterrupManager,iOQueue,quantum,programLoader,handlerIO,
                 #handlerList,scheduler,timeOutHandler,handlerKill,clock):
        self.handlerList = None #handlerList
        self.hd = None #hd
        self.mem = None #mem
        self.readyQueue = None #readyQueue
        self.kernel = None #kernel
        self.cpu = None #cpu 
        self.iOManager = None #iOManager
        self.interrupManager = None #InterrupManager
        self.iOQueue = None #iOQueue
        self.scheduler = None #scheduler
        self.quantum = None #quantum 
        self.handlerIO = None #handlerIO
        self.timeOutHandler = None #timeOutHandler
        self.programLoader = None #programLoader
        self.handlerList = None #handlerList
        self.handlerKill = None #handlerKill
        self.clock = None #clock