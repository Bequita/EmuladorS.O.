'''
Created on 30 de set. de 2015

@author: matutee
'''
from Code.Instruction import Instruction, InstructionKind
from Code.Program import Program
from Code.HardDisk import HardDisk
from Code.Memory import Memory

class SetUpMixin(object):

    def __init__(self):
        self.ins1 = Instruction("Primera instruccion ejecutada de CPU", InstructionKind.CPU)
        self.IOins1 = Instruction("PRIMERA INSTRUCCION DE IO", InstructionKind.IO)
        self.ins2 = Instruction("Segunda instruccion ejecutada de CPU", InstructionKind.CPU)
        self.ins3 = Instruction("Tercera instruccion ejecutada de CPU", InstructionKind.CPU)
        self.IOins2 = Instruction("SEGUNDA INSTRUCCION DE IO", InstructionKind.IO)
        
        self.prg = Program("PrimerPrograma", [self.ins1,self.IOins1,self.ins2,self.ins3,self.IOins2])
        self.hd = HardDisk()
        self.mem = Memory()
