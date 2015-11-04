'''
Created on 30 de set. de 2015

@author: matutee
'''
from Code.Instruction import Instruction, InstructionKind
from Code.Program import Program
from Code.HardDisk import HardDisk
from Code.Memory import Memory
from Code.IOHandler import IOHandler
from Code.KillHandler import KillHandler
from Code.TimeOutHandler import TimeOutHandler
from Code.InterruptionManager import InterruptionManager


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
        self.killHandler = KillHandler()
        self.timeOutHandler = TimeOutHandler()
        self.ioHandler = IOHandler
        self.handlerList = []
        self.handlerList.append(self.killHandler)
        self.handlerList.append(self.timeOutHandler)
        self.handlerList.append(self.ioHandler)
        self.interruptionManager = InterruptionManager() 
        #self.cpu = CPU(self.mem, self.interruptionManager)
    
