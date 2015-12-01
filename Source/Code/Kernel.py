from Code.ProgramLoader import ProgramLoader
from Code.Interruption import IRQ,IRQKind
from threading import Thread
from operator import eq

class Kernel(Thread):

    def __init__(self, prLoader, intManager, scheduler, cpu):
        Thread.__init__(self)
        self.interruptionManager = intManager
        self.scheduler = scheduler 
        self.cpu = cpu

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
                        
    def contextSwitching(self):
        if (self.cpu.context == "userMode"):
            self.cpu.context = "kernelMode"
        else:
            self.cpu.context = "userMode"
    
    def executeInterruptions(self):
    #    self.contextSwitching()
        #hasta que no termina de atender todas las interrupciones no pone modo usuario
        print("se va a ejecutar la instruccion")
        self.interruptionManager.executeInterruption()
    #    self.contextSwitching()
        #self.scheduler.startScheduler()
        #print("hice un tick")
    
    def run(self):
        while(True):
            #print(self.cpu.context)
            if(self.interruptionManager.irqList.__len__() > 0):
                #self.contextSwitching()
                self.executeInterruptions()
                print("estoy haciendo interrupciones")
                #self.contextSwitching()
                self.cpu.context = "userMode"
                self.scheduler.schedulerAssing.release()
                #self.cpu.mutexFetch.release()
            else:
                #print("kernel mando a ejecutar a cpu")
                #self.cpu.mutexFetch.release()
                self.cpu.execute()
            print("estoy vivo")
        
         
            