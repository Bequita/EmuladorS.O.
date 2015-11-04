from Code.Interruption import IRQ, IRQKind
from Code.Instruction import InstructionKind
from Code.InterruptionManager import InterruptionManager

class CPU(object):

    def __init__(self, mem, interrManager,scheduller):
        self.memory = mem
        self.interruptionManager = interrManager
        self.pcbLoaded = None
        self.context = "modeCPU"
        self.quantum = 0

    def asignPCB(self, pcb, quantum): # quantum enviado desde scheduler
        self.pcbLoaded = pcb
        self.quantum = quantum

    def execute(self):
        while(self.quantum > 0):
            self.quantum -= 1
            if(self.pcbLoaded != None or self.context.__eq__("modeCPU")):
            #if(self.existsNextMemoryPosition(self)):
                currentInstruction = self.fetch()
                # Determino si la instruccion es de tipo: CPU --> La ejecuto; IO --> Se lo paso al Interruption Manager para que lo meta en la IOQueue
                if(currentInstruction.getKind() == InstructionKind.CPU):
                    self.executeCPUInstruction(currentInstruction)
                elif(currentInstruction.getKind() == InstructionKind.IO):
                        #self.pcbLoaded.programCounter = self.pcbLoaded.programCounter + 1 # es asi ?
                        self.interruptionManager.handle()
                else:
                        raise NameError('Instruccion desconocida')
                
        ## LOS DOS METODOS self.memory.imprimirMemoria() HAY QUE SACARLOS, LOS DEJO SIMPLEMENTE PARA QUE VEAN QUE SE LIMPIA EL STACK DE MEMORIA
        self.memory.imprimirMemoria()
        # Termina la ejecucion del pcb, y llamo al KillHandler
        #self.interruptionManager.handle(IRQ(self.pcbLoaded, IRQKind.KILL))
        #self.memory.imprimirMemoria()

    #def existsNextMemoryPosition(self):
        #return (self.pcbLoaded.programCounter < self.pcbLoaded.programSize)

    def executeCPUInstruction(self,currentInstruction):
        currentInstruction.printIns()
        if(self.lastInstruction):
            self.interruptionManager.handle(IRQ(self.pcbLoaded, IRQKind.KILL))
            self.cpu.pcbLoader = None
        elif(self.scheduller.quantum.__eq__(0)):
            self.interruptionManager.handle(IRQ(self.pcbLoaded, IRQKind.TIMEOUT))
            self.cpu.pcbLoader = None
        else: 
            # Determino la proxima direccion de memoria de la siguiente instruccion
            self.pcbLoaded.programCounter = self.pcbLoaded.programCounter + 1
                        
    def fetch(self):
        return self.memory.fetchMem(self.pcbLoaded.baseDirection + self.pcbLoaded.programCounter)

    def lastInstruction(self):
        return (self.pcbLoaded.programCounter - self.pcbLoaded.baseDirection + 1).__eq__(self.pcbLoaded.programSize)
        
