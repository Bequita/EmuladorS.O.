from Code.Interruption import IRQ, IRQKind
from Code.Instruction import InstructionKind

class CPU(object):

    def __init__(self, mem, interrManager):
        self.memory = mem
        self.interruptionManager = interrManager
        self.pcbLoaded = None

    def asignPCB(self, pcb):
        self.pcbLoaded = pcb

    def execute(self):
        if(self.existsNextMemoryPosition(pcb)):
            currentInstruction = self.fetch(pcb)

            # Determino si la instruccion es de tipo: CPU --> La ejecuto; IO --> Se lo paso al Interruption Manager para que lo meta en la IOQueue
            if(currentInstruction.getKind() == InstructionKind.CPU):
                currentInstruction.printIns()
            elif(currentInstruction.getKind() == InstructionKind.IO):
                self.interruptionManager.handle()
            else:
                raise NameError('Instruccion desconocida')

            # Determino la proxima direccion de memoria de la siguiente instruccion
            pcb.programCounter = pcb.programCounter + 1

        ## LOS DOS METODOS self.memory.imprimirMemoria() HAY QUE SACARLOS, LOS DEJO SIMPLEMENTE PARA QUE VEAN QUE SE LIMPIA EL STACK DE MEMORIA
        self.memory.imprimirMemoria()
        # Termina la ejecucion del pcb, y llamo al KillHandler
        self.interruptionManager.handle(IRQ(pcb, IRQKind.KILL))
        self.memory.imprimirMemoria()

    def existsNextMemoryPosition(self, pcb):
        return (pcb.programCounter < pcb.programSize)

    def fetch(self, pcb):
        return self.memory.fetchMem(pcb.baseDirection + pcb.programCounter)
