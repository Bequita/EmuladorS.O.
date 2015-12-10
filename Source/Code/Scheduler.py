
class Scheduler(object):
    def __init__(self, sistemComponents):
        self.cpu = sistemComponents.cpu
        self.quantum = sistemComponents.quantum
        self.readyQueue = sistemComponents.readyQueue
        
    def assignPCB(self):
        print("ejecuto scheduler")
        pcb = self.readyQueue.getPcb()
        self.cpu.assignPCB(pcb,self.quantum)
    
    def printReadyQueue(self):
        print(" ")
        print("PRIORIDAD 1 CADA UNO DE SUS NIVELES")
        print(self.readyQueue.estrategy.priorities[1].level1)
        print(self.readyQueue.estrategy.priorities[1].level2)
        print(self.readyQueue.estrategy.priorities[1].level3)
        print("")
        print("PRIORIDAD 2 CADA UNO DE SUS NIVELES")
        print(self.readyQueue.estrategy.priorities[2].level1)
        print(self.readyQueue.estrategy.priorities[2].level2)
        print(self.readyQueue.estrategy.priorities[2].level3)
        print("")
        print("PRIORIDAD 3 CADA UNO DE SUS NIVELES")
        print(self.readyQueue.estrategy.priorities[3].level1)
        print(self.readyQueue.estrategy.priorities[3].level2)
        print(self.readyQueue.estrategy.priorities[3].level3)
        
    def addPCB(self,pcb):
        self.readyQueue.addPcb(pcb)
        print("le di la interrupcion a readyQueue")
        self.printReadyQueue()