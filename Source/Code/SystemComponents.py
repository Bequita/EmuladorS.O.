from Code.HardDisk import HardDisk
from Code.Memory import Memory
from Code.ReadyQueue import ReadyQueue
from Code.InterruptionManager import InterruptionManager
from Code.TimeOutHandler import TimeOutHandler

class SystemComponents(object):

    def __init__(self,kernel,cpu,hd,mem,readyQueue,iOManager,InterrupManager,iOQueue,quantum,programLoader,handlerIO,
                 TimeOutHandler,handlerList,scheduler,timeOutHandler,handlerKill,clock):
        self.handlerList = handlerList
        self.hd = hd
        self.mem = mem
        self.readyQueue = readyQueue
        self.kernel = kernel
        self.cpu = cpu 
        self.iOManager = iOManager
        self.interrupManager = InterrupManager
        self.iOQueue = iOQueue
        self.scheduler = scheduler
        self.quantum = quantum 
        self.handlerIO = handlerIO
        self.timeOutHandler = timeOutHandler
        self.programLoader = programLoader
        self.handlerList = handlerList
        self.handlerKill = handlerKill
        self.clock = clock