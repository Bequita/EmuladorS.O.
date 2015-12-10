from Code.Interruption import IRQ, IRQKind
from Code.Instruction import InstructionKind
from threading import Condition
from Code.Kernel import Kernel

class CPU(object):

    def __init__(self, systemComponents):
        self.memory = systemComponents.mem
        self.interruptionManager = systemComponents.interrupManager
        self.pcbLoaded = None
        self.quantum = 0
        self.ticks= 4
        self.counter=0
        self.mutex = Condition()
        self.kernel = systemComponents.kernel

    def assignPCB(self, pcb, quantum): # quantum enviado desde scheduler
        self.pcbLoaded = pcb
        self.quantum = quantum
        print("scheduler me dio: " + pcb.programName.__str__())

    def process(self):
        if(self.quantum == 0 and self.pcbLoaded == None):
            self.kernel.modeSwitching()
            print("Nada para ejecutar")
        elif(self.canExecute()):
            print("CPU va a ejecutar el PCB")
            currentInstruction = self.fetch()
            self.executeCurrentInstruction(currentInstruction)
            print("La instruccion es: " + self.fetch().getMessage())
        else:
            print("Nada para ejecutar")
        self.quantum -= 1
    
    def executeCurrentInstruction(self,currentInstruction):
        # Determino si la instruccion es de tipo: CPU --> La ejecuto; IO --> Se lo paso al Interruption Manager para que lo meta en la IOQueue
        if(currentInstruction.getKind() == InstructionKind.CPU):
            print("La instruccion es de CPU, La ejecuta CPU")
            self.executeCPUInstruction(currentInstruction)
        elif(currentInstruction.getKind() == InstructionKind.IO):
            print("La instruccion es de IOManager, La ejecuta IOManager")
            self.executeIOInstruction(currentInstruction)
            #self.iOManager.add(IRQ(self.pcbLoaded, IRQKind.IO))
            #self.pcbLoaded.nextInstruction = self.pcbLoaded.nextInstruction + 1
        else:
            raise NameError('Instruccion desconocida')
          
    def execute(self):
        print("quiere ejecutar cpu el modo es: " + self.kernel.mode.__str__())
        while(self.kernel.mode == Kernel.USER):
            with self.mutex:
                self.mutex.wait()
                print("comienza a ejecutar")
                self.process()
    
    def canExecute(self):
        return self.pcbLoaded != None and self.kernel.mode == Kernel.USER 

    def executeIOInstruction(self,currentInstruction):
        if(self.lastInstruction()):
            self.pcbLoaded = None
        self.pcbLoaded.nextInstruction = self.pcbLoaded.nextInstruction + 1
        self.iOManager.add(IRQ(self.pcbLoaded, IRQKind.IO))

    def executeCPUInstruction(self,currentInstruction):
        # Determino la proxima direccion de memoria de la siguiente instruccion
        self.pcbLoaded.nextInstruction = self.pcbLoaded.nextInstruction + 1
        if(self.lastInstruction()):
            self.kernel.addInterruption(IRQ(self.pcbLoaded, IRQKind.KILL))
            self.pcbLoader = None
        elif(self.quantum == 0):
            self.interruptionManager.addInterruption(IRQ(self.pcbLoaded, IRQKind.TIMEOUT))
            self.pcbLoader = None
                        
    def fetch(self):
        print("next instruction: " + self.pcbLoaded.nextInstruction.__str__())
        return self.memory.fetch(self.pcbLoaded, self.pcbLoaded.nextInstruction)

    def lastInstruction(self):
        return (self.pcbLoaded.nextInstruction + 1 == self.pcbLoaded.programSize)
        
