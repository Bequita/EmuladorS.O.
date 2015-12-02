'''
Created on 30 de set. de 2015

@author: matutee
'''
from Code.CPU import CPU
from Code.Clock import Clock
from Code.HardDisk import HardDisk
from Code.IOHandler import IOHandler
from Code.IOHandler import IOHandler
from Code.IOManager import IOManager
from Code.IOQueue import IOQueue
from Code.IOQueue import IOQueue
from Code.Instruction import Instruction, InstructionKind
from Code.InterruptionManager import InterruptionManager
from Code.InterruptionManager import InterruptionManager
from Code.Kernel import Kernel
from Code.KillHandler import KillHandler
from Code.KillHandler import KillHandler
from Code.Memory import Memory
from Code.NewPCBHandler import NewPCBHandler
from Code.PCB import PCB
from Code.PCB import PCB
from Code.Program import Program
from Code.ProgramLoader import ProgramLoader
from Code.ProgramLoader import ProgramLoader
from Code.ReadyQueue import CeldaEnvejecimiento
from Code.ReadyQueue import ReadyQueue
from Code.ReadyQueue import ReadyQueue
from Code.Scheduler import Scheduler
from Code.TimeOutHandler import TimeOutHandler


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
        self.ioHandler = IOHandler
        self.handlerList = []
        self.handlerList.append(self.killHandler)
        self.handlerList.append(self.timeOutHandler)
        self.handlerList.append(self.ioHandler)
        self.interruptionManager = InterruptionManager()
        self.cpu = CPU(self.mem, self.interruptionManager) 
        self.readyQueue = CeldaEnvejecimiento()
        self.scheduler = Scheduler(self.cpu,4,self.readyQueue)
        self.programLoader = ProgramLoader(self.hd,self.mem,self.readyQueue)
        self.kernel = Kernel(self.programLoader,self.interruptionManager)
    
    
def main():
    ins1 = Instruction("PRIMERA INSTRUCCION EJECUTADA DE CPU", InstructionKind.CPU)
    #IOins1 = Instruction("PRIMERA INSTRUCCION DE IO", InstructionKind.IO)
    ins2 = Instruction("SEGUNDA INSTRUCCION EJECUTADA DE CPU", InstructionKind.CPU)
    ins3 = Instruction("TERCERA INSTRUCCION EJECUTADA DE CPU", InstructionKind.CPU)
    #IOins2 = Instruction("SEGUNDA INSTRUCCION DE IO", InstructionKind.IO)
    
    listIntruction = []
    listIntruction.append(ins1)
    listIntruction.append(ins2)
    listIntruction.append(ins3)
    prg = Program("PrimerPrograma", listIntruction)
    hd = HardDisk()
    hd.addProgram(prg)
    mem = Memory()
    
    readyQueue = ReadyQueue()
    
    iOQueue = IOQueue()
    ioHandler = IOHandler(iOQueue,mem)
    handlerList = []
    handlerList.append(ioHandler)
    timeOutHandler = TimeOutHandler(readyQueue)
    handlerList.append(timeOutHandler)
    
    scheduler = Scheduler(None,2,readyQueue)
    interruptionManager = InterruptionManager(handlerList)
    programLoader = ProgramLoader(hd,mem,readyQueue)
    
    
    iOManager = IOManager(ioHandler)
    
    cpu = CPU(mem,interruptionManager,scheduler,iOManager)
    kernel = Kernel(programLoader,interruptionManager,scheduler,cpu)  
    scheduler.cpu=cpu
    
    
    clock = Clock(cpu,iOManager)
    
    killHandler = KillHandler(mem,kernel)
    handlerList.append(killHandler)
    
    mem.loadProgram(prg)
    print(mem.capacity)
    
    killHandler = KillHandler(mem,kernel)
    interruptionManager.handlersList.append(killHandler)
    programLoader.loadProgram("PrimerPrograma")
    
    #scheduler.start()    
    kernel.start()
    iOManager.start()
    
    clock.start()
    #kernel.start()
    #scheduler.start()
    
main()

