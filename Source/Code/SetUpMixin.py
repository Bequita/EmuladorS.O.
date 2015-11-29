'''
Created on 30 de set. de 2015

@author: matutee
'''
from Code.Instruction import Instruction, InstructionKind
from Code.Program import Program
from Code.HardDisk import HardDisk
from Code.Memory import Memory
from Code.PCB import PCB
from Code.ProgramLoader import ProgramLoader
from Code.InterruptionManager import InterruptionManager
from Code.IOHandler import IOHandler
from Code.ReadyQueue import ReadyQueue
from Code.IOQueue import IOQueue
from Code.KillHandler import KillHandler
from Code.NewPCBHandler import NewPCBHandler
from Code.IOHandler import IOHandler
from Code.KillHandler import KillHandler
from Code.TimeOutHandler import TimeOutHandler
from Code.InterruptionManager import InterruptionManager


class SetUpMixin(object):

    def __init__(self):
        # Instrucciones
        self.ins1 = Instruction("Primera instruccion ejecutada de CPU", InstructionKind.CPU)
        self.IOins1 = Instruction("PRIMERA INSTRUCCION DE IO", InstructionKind.IO)
        self.ins2 = Instruction("Segunda instruccion ejecutada de CPU", InstructionKind.CPU)
        self.ins3 = Instruction("Tercera instruccion ejecutada de CPU", InstructionKind.CPU)
        self.IOins2 = Instruction("SEGUNDA INSTRUCCION DE IO", InstructionKind.IO)
        
        # Programas con su lista de instrucciones
        self.prg1 = Program("PrimerPrograma", [self.ins1,self.IOins1,self.ins2,self.ins3,self.IOins2], 2, 1)
        self.prg2 = Program("SegundoPrograma", [self.ins1,self.IOins1,self.ins2,self.ins3], 2, 2)
        
        # Colas
        self.readyQueue = ReadyQueue()
        self.IOQueue = IOQueue()
        
        # Disco rigido
        self.hd = HardDisk()
        
        # Memoria
        self.mem = Memory(4, 2)
        
        # Handlers de las interrupciones
        self.ioHandler = IOHandler(self.IOQueue, self.mem)
        self.timeOutHandler = TimeOutHandler()
        self.killHandler = KillHandler(self.mem, None)
        self.newPcbHandler = NewPCBHandler(self.readyQueue)
        
        # Interruption Manager, con sus handlers registrados
        self.interruptionManager = InterruptionManager()
        self.interruptionManager.registerHandler(self.ioHandler)
        self.interruptionManager.registerHandler(self.timeOutHandler)
        self.interruptionManager.registerHandler(self.killHandler)
        self.interruptionManager.registerHandler(self.newPcbHandler)
        
        # Program Loader
        self.prLoader = ProgramLoader(self.hd, self.mem, self.interruptionManager)
        
        #self.mem = Memory()
        #self.killHandler = KillHandler()
        #self.timeOutHandler = TimeOutHandler()
        #self.ioHandler = IOHandler
        #self.handlerList = []
        #self.handlerList.append(self.killHandler)
        #self.handlerList.append(self.timeOutHandler)
        #self.handlerList.append(self.ioHandler)
        #self.interruptionManager = InterruptionManager() 
        #self.cpu = CPU(self.mem, self.interruptionManager)
    