from Code.ProgramLoader import ProgramLoader
from threading import Thread

class Kernel(Thread):

    def __init__(self, prLoader, intManager):
        self.interruptionManager = intManager

    def loadProgramToPL(self, programName):
        self.programLoader.loadProgram(programName)

    def handle(self, pcb):
        # Cuando se ejecuta una interrupcion dentro de CPU
        # El scheduler le da a CPU el siguiente PCB de QReady
        self.scheduler.changePCB()
        # Me fijo el tipo de la interrrupcion
        self.interruptionManager.handle(IRQ(pcb, IRQKind."TIPO"))

    def killRoutine(self,pcb):
        self.contextSwitching()
        self.freeMemory(pcb)
        #freeCPU() lo hace cpu
        self.contextSwitching()
        self.scheduler.assignPCB()
            
    
    def freeMemory(self,pcb):
        self.memory.cleanMemoryFromPointer(pcb().baseDirection, pcb().programSize)    
                        
    def contextSwitching(self):
        if(self.cpu.context == "modeCPU"):
            self.cpu.context = "modeKernel"
        else:
            self.cpu.context = "modeCPU"
    
    def tickKernel(self):
        self.interruptionManager.
            