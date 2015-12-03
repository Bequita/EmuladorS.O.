from Code.CPU import CPU


class SystemComponents(object):

    def __init__(self,kernel,cpu,mem,iOManager,interrupManager,iOQueue,scheduler,quantum,readyQueue):
        self.kernel = kernel
        self.cpu = cpu 
        self.mem = mem
        self.iOMnager = iOManager
        self.interrupManager = interrupManager
        self.iOQueue = iOQueue
        self.scheduler = scheduler
        self.quantum = quantum 
        self.readyQueue = readyQueue 