from Code.Interruption import IRQ, IRQKind
from Code.Instruction import InstructionKind
import threading
import time

class CPU(object):

    def __init__(self, mem, interrManager,scheduler, iOManager):
        self.memory = mem
        self.interruptionManager = interrManager
        self.pcbLoaded = None
        self.context = "userMode"
        self.quantum = 0
        self.ticks= 4
        self.counter=0
        self.mutex = threading.Semaphore(0)
        self.iOManager = iOManager
        self.scheduler = scheduler
        

    def assignPCB(self, pcb, quantum): # quantum enviado desde scheduler
        self.pcbLoaded = pcb
        self.quantum = quantum

    def execute(self):
        while(self.quantum > 0):
            self.mutex.acquire
            print(self.quantum)
            print("va a ejecutar cpu ")
            print(self.pcbLoaded == None)
            print(self.context)
            self.quantum -= 1
            if(self.pcbLoaded != None and self.context=="userMode"):
                print("ejecuto cpu")
            #if(self.existsNextMemoryPosition(self)):
                currentInstruction = self.fetch()
                print(self.fetch().getMessage() + " es la instruccion")
                print(currentInstruction.getMessage())
                # Determino si la instruccion es de tipo: CPU --> La ejecuto; IO --> Se lo paso al Interruption Manager para que lo meta en la IOQueue
                if(currentInstruction.getKind() == InstructionKind.CPU):
                    print("La instruccion es de CPU, La ejecuta CPU")
                    self.executeCPUInstruction(currentInstruction)
                elif(currentInstruction.getKind() == InstructionKind.IO):
                        #self.pcbLoaded.programCounter = self.pcbLoaded.programCounter + 1 # es asi ?
                        print("La instruccion es de IOManager, La ejecuta IOManager")
                        self.iOManager.add(IRQ(self.pcbLoaded, IRQKind.IO))
                        self.pcbLoaded.programCounter = self.pcbLoaded.programCounter + 1
                        #self.context = "kernelMode"
                else:
                        raise NameError('Instruccion desconocida')
                
        ## LOS DOS METODOS self.memory.imprimirMemoria() HAY QUE SACARLOS, LOS DEJO SIMPLEMENTE PARA QUE VEAN QUE SE LIMPIA EL STACK DE MEMORIA
            else:
                print("Nada para ejecutar")
                time.sleep(1)
        # Termina la ejecucion del pcb, y llamo al KillHandler
        #self.interruptionManager.handle(IRQ(self.pcbLoaded, IRQKind.KILL))
        #self.memory.imprimirMemoria()

    #def existsNextMemoryPosition(self):
        #return (self.pcbLoaded.programCounter < self.pcbLoaded.programSize)
    
    def executeIOInstruction(self,currentInstruction):
        if(self.quantum.__eq__(0)):
            print("-- kill --")
            
        

    def executeCPUInstruction(self,currentInstruction):
        currentInstruction.printIns()
        print(self.pcbLoaded.programCounter)
        print(self.pcbLoaded.baseDirection)
        print(self.pcbLoaded.programSize)
        print(self.lastInstruction())
        if(self.lastInstruction()==True):
            self.interruptionManager.addInterruption(IRQ(self.pcbLoaded, IRQKind.KILL))
            self.pcbLoader = None
            print("entro por kill")
            self.context = "kernelMode"
        elif(self.quantum.__eq__(0)):
            self.interruptionManager.addInterruption(IRQ(self.pcbLoaded, IRQKind.TIMEOUT))
            self.pcbLoader = None
            self.context = "kernelMode"
        #else: 
            # Determino la proxima direccion de memoria de la siguiente instruccion
        self.pcbLoaded.programCounter = self.pcbLoaded.programCounter + 1
                        
    def fetch(self):
        return self.memory.fetchMem(self.pcbLoaded.baseDirection + self.pcbLoaded.programCounter)

    def lastInstruction(self):
        return (self.pcbLoaded.programCounter + 1 == self.pcbLoaded.programSize)
        
