'''
Created on 30 de set. de 2015
@author: matutee
'''
from Code.CPU import CPU
from Code.Clock import Clock
from Code.HardDisk import HardDisk
from Code.IOHandler import IOHandler
from Code.IOManager import IOManager
from Code.IOQueue import IOQueue
from Code.Instruction import Instruction, InstructionKind
from Code.InterruptionManager import InterruptionManager
from Code.Kernel import Kernel
from Code.KillHandler import KillHandler
from Code.Memory import Memory
from Code.NewPCBHandler import NewPCBHandler
from Code.PCB import PCB
from Code.Program import Program
from Code.ProgramLoader import ProgramLoader
from Code.ReadyQueue import PriorityQueue
from Code.ReadyQueue import ReadyQueue
from Code.Scheduler import Scheduler
from Code.TimeOutHandler import TimeOutHandler
from Code.SystemComponents import SystemComponents


class SetUpMemoria(object):

    def __init__(self):
       pass
       
def main():
    
    quantum = 4
    #so = None
    so = SystemComponents()
    
    ins1 = Instruction("PRIMERA INSTRUCCION EJECUTADA DE CPU", InstructionKind.CPU)
    iOins1 = Instruction("PRIMERA INSTRUCCION DE IO", InstructionKind.IO)
    ins2 = Instruction("SEGUNDA INSTRUCCION EJECUTADA DE CPU", InstructionKind.CPU)
    ins3 = Instruction("TERCERA INSTRUCCION EJECUTADA DE CPU", InstructionKind.CPU)
    #IOins2 = Instruction("SEGUNDA INSTRUCCION DE IO", InstructionKind.IO)
    
    listIntruction = []
    listIntruction.append(ins1)
    listIntruction.append(iOins1)
    listIntruction.append(ins2)
    listIntruction.append(ins3)
    prg1 = Program("PrimerPrograma", listIntruction, 2, 2) 
    prg1.instructionsToPages()
        
    so.readyQueue = ReadyQueue(PriorityQueue())
    so.quantum = quantum
    so.hd = HardDisk()
    so.hd.addProgram(prg1)
    so.mem = Memory(4,2,so.hd)
    so.mem.hardDisk = so.hd
    so.cpu = CPU(so)
    so.scheduler = Scheduler(so)
    so.scheduler.readyQueue = so.readyQueue
    so.scheduler.cpu = so.cpu
    so.scheduler.quantum = so.quantum
    so.newPCBHandler = NewPCBHandler(so)
    so.newPCBHandler.scheduler = so.scheduler
    so.iOQueue = IOQueue()
    so.handlerIO = IOHandler(so)
    so.handlerIO.iOQueue
    so.handlerIO.memory = so.mem
    so.timeOutHandler = TimeOutHandler(so)
    so.handlerKill = KillHandler(so)
    so.handlerList = []
    so.handlerList.append(so.timeOutHandler)
    so.handlerList.append(so.handlerIO)
    so.handlerList.append(so.handlerKill)
    so.handlerList.append(so.newPCBHandler)
    so.interrupManager = InterruptionManager(so)
    so.kernel = Kernel(so)
    so.interrupManager.kernel = so.kernel
    so.kernel.interruptionManager = so.interrupManager
    so.cpu.kernel = so.kernel
    so.kernel.cpu = so.cpu
    so.cpu.scheduler = so.scheduler
    so.cpu.interruptionManager = so.interrupManager
    so.cpu.memory = so.mem
    so.scheduler.cpu = so.cpu
    so.iOManager = IOManager(so)
    so.cpu.iOManager = so.iOManager
    
    so.programLoader = ProgramLoader(so)
    so.cpu.pcbLoaded = so.programLoader
    so.programLoader.scheduler = so.scheduler
    so.clock = Clock(so)    
    
    so.programLoader.loadProgram("PrimerPrograma")
    so.programLoader.interruptionManager = so.kernel.interruptionManager
    
    so.kernel.start()
    so.iOManager.start()
    so.clock.start()
    
main()