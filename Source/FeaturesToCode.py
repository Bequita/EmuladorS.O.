'''
Created on 15 de set. de 2015

@author: matutee
'''
from Instruction import Instruction, InstructionKind
from PCB import PCB
import Memory
from CPU import CPU
from InterruptionManager import InterruptionManager
from KillHandler import KillHandler
from IOQueue import IOQueue
from IOHandler import IOHandler

'''
******************* GUIA MIA ******************

1) Crear InstructionManager

    Metodos:
        - register(KindHandler) --> Registro el handler de cada tipo de interrupcion de IRQ
        
2) Crear handlers de cada tipo de IRQKind.
    
    Metodos:
        - canHandle(Instruccion) --> retorna un bool que dice si puede manejar ese tipo de instr.
        - handle(new IRQ(Kind, pcb)) --> Itera en la lista de Handlers, si hay alguno que pueda resolverla lo resuelve. Sino lanza excepcion. 

        
******************* GUIA DE PASOS QUE ESCRIBIO NANDO ******************

cpu ---> 
      irq = new IRQ(IRQKind.KILL, pcb) 
      im.handle(irq)

KillHandler()
IOHandler()
TimeoutHandler()

class IM():
    
    def _init_(self, ):

    def register(self, Handler):
        list.add(hanlder)
     
            
                                  
im.register(new KillHandler())
KillHandler.canHandle(int)

--------------- Setup SO -----------
im=new Interuptionmanager()
im.register(IRQKind.KILL, new KillHandler())
im.register(IRQKind.IO, new IOHandler())
--------------------------


-->  im.handle(irq (KILL, pcb))
           ---> KillHandler.handle(pcb)

-->  im.handle(irq (IO, pcb))
           ---> IOHandler.handle(pcb)
'''

# INSTANCIACION Y PUESTA EN PRACTICA DE TODO LO VISTO EN CLASE HOY.
# Si quieren que la cpu ejecute instrucciones de manera atomica, cambien el while por un if, SHORT ! ! ! 

IOq = IOQueue()
mem = Memory.Memory()

ins1 = Instruction("Primera instruccion ejecutada de CPU", InstructionKind.CPU)
IOins1 = Instruction("PRIMERA INSTRUCCION DE IO", InstructionKind.IO)
ins2 = Instruction("Segunda instruccion ejecutada de CPU", InstructionKind.CPU)
ins3 = Instruction("Tercera instruccion ejecutada de CPU", InstructionKind.CPU)
IOins2 = Instruction("SEGUNDA INSTRUCCION DE IO", InstructionKind.IO)

pcb = PCB(0,5, [ins1, IOins1, ins2, ins3, IOins2])

mem.loadInstructions(pcb.instructions, pcb.baseDirection)

intrMan = InterruptionManager()
intrMan.registerHandler(KillHandler(mem))
intrMan.registerHandler(IOHandler(IOq, mem))

cpu = CPU(mem, intrMan)
cpu.execute(pcb)

# Esto indica el largo de la cola de IO, deberia ser dos en este caso
print(IOq.getQueue().__len__())