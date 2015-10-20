'''
Created on 15 de set. de 2015

@author: matutee
'''

from Instruction import Instruction, InstructionKind
from Memory import Memory
from Program import Program
from ProgramLoader import ProgramLoader
from HardDisk import HardDisk
from ReadyQueue import ReadyQueue
from CPU import CPU
from InterruptionManager import InterruptionManager
from KillHandler import KillHandler
from IOQueue import IOQueue
from IOHandler import IOHandler
'''
******************* GUIA DE COSAS A IMPLEMENTAR ******************

OBJETOS QUE NOS FALTAN:

1) el objeto que va a llevar a llevar a cabo la IOInterruption, es decir, el que va a resolver esa interrupcion 
y va a volver a meter el PCB en la cola de Ready.

2) El clock de la CPU

3) Dos interrupciones mas: IOFinished y NewPCB.

4) Scheduler. Y su respectiva logica de asignacion de PCB's a CPU (RoundRobin con PriorityQueue).
Dato: Python ya trae una PriorityQueue por defecto. Habria que ver la implementacion de la misma, y quiza podamos usarla...

******************************************************************        
'''

# INSTANCIACION Y PUESTA EN PRACTICA DE TODO LO VISTO EN CLASE HOY.
# Si quieren que la cpu ejecute instrucciones de manera atomica, cambien el while por un if, SHORT ! ! ! 

IOq = IOQueue()
RQ = ReadyQueue()
mem = Memory()
hd = HardDisk()

prLoader = ProgramLoader(hd, mem, RQ)

ins1 = Instruction("Primera instruccion ejecutada de CPU", InstructionKind.CPU)
IOins1 = Instruction("PRIMERA INSTRUCCION DE IO", InstructionKind.IO)
ins2 = Instruction("Segunda instruccion ejecutada de CPU", InstructionKind.CPU)
ins3 = Instruction("Tercera instruccion ejecutada de CPU", InstructionKind.CPU)
IOins2 = Instruction("SEGUNDA INSTRUCCION DE IO", InstructionKind.IO)

prg = Program("PrimerPrograma", [ins1,IOins1,ins2,ins3,IOins2])
hd.addProgram(prg)

prLoader.loadProgram("PrimerPrograma")

intrMan = InterruptionManager()
intrMan.registerHandler(KillHandler(mem))
intrMan.registerHandler(IOHandler(IOq, mem))

cpu = CPU(mem, intrMan)
cpu.execute(RQ.pcbs._get())

# Esto indica el largo de la cola de IO, deberia ser dos en este caso
print(IOq.getQueue().__len__())