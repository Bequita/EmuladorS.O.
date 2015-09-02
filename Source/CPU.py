'''
Created on 1 de set. de 2015

@author: matutee
'''
import Instruction
from PCB import PCB
import RaiseHandler
import Memory
import CPU

class CPU(object):

    def __init__(self, mem, handler):
        self.memory = mem
        self.raiseHandler = handler
        
    def execute(self, pcb):
        while(pcb.programCounter < pcb.programSize):
            self.memory.executeMem(pcb.baseDirection + pcb.programCounter)
            pcb.programCounter = pcb.programCounter + 1
        self.raiseHandler.finished()

# INSTANCIACION Y PUESTA EN PRACTICA DE TODO LO VISTO EN CLASE HOY.
# Si quieren que la cpu ejecute instrucciones de manera atomica, cambien el while por un if, LA CONCHA DE SU MADRE ! ! ! 


ins1 = Instruction.Instruction("Primera instruccion")
ins2 = Instruction.Instruction("Segunda instruccion")
ins3 = Instruction.Instruction("Tercera instruccion")
pcb = PCB(0,3, [ins1, ins2, ins3])

mem = Memory.Memory()
mem.loadInstructions(pcb.instructions, pcb.baseDirection)

raiseHl = RaiseHandler.RaiseHandler()
cpu = CPU(mem, raiseHl)
cpu.execute(pcb)
