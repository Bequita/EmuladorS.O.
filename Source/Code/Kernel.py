from Code.ProgramLoader import ProgramLoader
from Code.Interruption import IRQ,IRQKind
from threading import Thread
from operator import eq

class Kernel(Thread):
      
    USER = "userMode"
    KERNEL = "kernelMode"

    def __init__(self, systemComponents):
        Thread.__init__(self)
        self.interruptionManager = systemComponents.interrupManager
        self.scheduler = systemComponents.scheduler 
        self.cpu = systemComponents.cpu
        self.mode = Kernel.KERNEL
        
    def addInterruption(self, interruption):
        self.mode = Kernel.KERNEL
        self.irqManager.addInterruption(interruption)

    def loadProgramToPL(self, programName):
        self.programLoader.loadProgram(programName)

    def handle(self, pcb):
        # Cuando se ejecuta una interrupcion dentro de CPU
        # El scheduler le da a CPU el siguiente PCB de QReady
        self.scheduler.assingPcb()
        # Me fijo el tipo de la interrrupcion
        #self.interruptionManager.handle(IRQ(pcb, IRQKind.getKind)  
        
    def freeMemory(self,pcb):
        self.memory.cleanMemoryFromPointer(pcb().baseDirection, pcb().programSize)    
                        
    def modeSwitching(self):
        if (self.mode == Kernel.USER):
            self.mode = Kernel.KERNEL
        else:
            self.mode = Kernel.USER
    
    def executeInterruptions(self):
        #hasta que no termina de atender todas las interrupciones no pone modo usuario
        self.interruptionManager.executeInterruption()
    
    def run(self):
        while(True):
            if(self.interruptionManager.irqList.__len__() > 0):
                self.executeInterruptions()
                print("ejecutando interrupciones")
            else:
                self.mode = Kernel.USER
                self.scheduler.assignPCB()
                self.cpu.execute()
        
         
            