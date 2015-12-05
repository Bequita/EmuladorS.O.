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


class SetUpMixinMaty(object):

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
        #self.readyQueue = CeldaEnvejecimiento()
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
    prg = Program("PrimerPrograma", listIntruction,3,2)
    hd = HardDisk()
    hd.addProgram(prg)
    
    mem = Memory(9,3,hd)
    
    readyQueue = ReadyQueue(PriorityQueue)
    
    iOQueue = IOQueue()
    #ioHandler = IOHandler(iOQueue,mem)
    #handlerList.append(ioHandler)
    #timeOutHandler = TimeOutHandler(readyQueue)
    #handlerList.append(timeOutHandler)
    
    #scheduler = Scheduler(None,2,readyQueue)
    #programLoader = ProgramLoader(hd,mem,readyQueue)
    
    
    #iOManager = IOManager(ioHandler)
    
    #cpu = CPU(mem,interruptionManager,scheduler,iOManager)
    #kernel = Kernel(programLoader,interruptionManager,scheduler,cpu)  
    #scheduler.cpu=cpu
    
    
    #clock = Clock(cpu,iOManager)
    
    #killHandler = KillHandler(mem,kernel)
    #handlerList.append(killHandler)
    
    #mem.loadProgram(prg)
    #print(mem.capacity)
    
    #killHandler = KillHandler(mem,kernel)
    #interruptionManager.handlersList.append(killHandler)
    #programLoader.loadProgram("PrimerPrograma")
    
    #scheduler.start()    
    quantum = 3
    #so = SystemComponents()
    #so.readyQueue = readyQueue
    #so.quantum = quantum
    #so.hd = hd
    #so.mem = mem
    #so.cpu = CPU(so)
    #so.scheduler = Scheduler(so)
    #so.newPCBHandler = NewPCBHandler(so)
    #so.handlerIO = IOHandler(so)
    #so.timeOutHandler = TimeOutHandler(so)
    #so.handlerKill = KillHandler(so)
    #so.handlerList = []
    #so.handlerList.append(so.timeOutHandler)
    #so.handlerList.append(so.handlerIO)
    #so.handlerList.append(so.handlerKill)
    #so.handlerList.append(so.newPCBHandler)
    #so.interrupManager = InterruptionManager(so)
    #so.kernel = Kernel(so)
    #so.cpu.kernel = so.kernel
    #so.iOManager = IOManager(so)
    #so.iOQueue = iOQueue

    #so.programLoader = ProgramLoader(so)
    #so.clock = Clock(so)    
    #print(so.handlerList)
    
    #so.programLoader.loadProgram("PrimerPrograma")
    
    #print(mem.blocksTable)
    #print(mem.blockSize)
    #print(mem.firstBlockFree())
    #print(mem.hardDisk)
    #print(mem.memoryBlocks)
    #print(mem.spaceFreeInMemory())
    
    #so.kernel.start()
    #so.iOManager.start()
    #so.clock.start()
    
    pcb1 = PCB(1,"PrimerPrograma",3,1)
    pcb2 = PCB(2,"segundoPrograma",3,2)
    pcb3 = PCB(3,"terceroPrograma",3,3)
    pcb4 = PCB(4,"cuartoPrograma",3,1)
    pcb5 = PCB(5,"quintoPrograma",3,2)
    pcb6 = PCB(6,"sextoPrograma",3,3)
    
    readyQueue = ReadyQueue(PriorityQueue())
    readyQueue.addPcb(pcb1)
    readyQueue.addPcb(pcb2)
    readyQueue.addPcb(pcb5)
    readyQueue.addPcb(pcb6)
    readyQueue.addPcb(pcb4)
    readyQueue.addPcb(pcb3)
    

    print(" ")
    print("PRIORIDAD 1 CADA UNO DE SUS NIVELES")
    print(readyQueue.estrategy.priorities[1].level1)
    print(readyQueue.estrategy.priorities[1].level2)
    print(readyQueue.estrategy.priorities[1].level3)
    print("")
    print("PRIORIDAD 2 CADA UNO DE SUS NIVELES")
    print(readyQueue.estrategy.priorities[2].level1)
    print(readyQueue.estrategy.priorities[2].level2)
    print(readyQueue.estrategy.priorities[2].level3)
    print("")
    print("PRIORIDAD 3 CADA UNO DE SUS NIVELES")
    print(readyQueue.estrategy.priorities[3].level1)
    print(readyQueue.estrategy.priorities[3].level2)
    print(readyQueue.estrategy.priorities[3].level3)
    print(" ")
    print("PEDIDO DE UN PCB -----------------------------")
    print("")
    print(readyQueue.getPcb().__str__() + " tiene que ser el pcb que esta mas abajo en las colas")
    print("")
    print("COLA DE READY DESPUES DE DAR EL PCB ----------")
    print("")
    
    print("PRIORIDAD 1 CADA UNO DE SUS NIVELES")
    print(readyQueue.estrategy.priorities[1].level1)
    print(readyQueue.estrategy.priorities[1].level2)
    print(readyQueue.estrategy.priorities[1].level3)
    print("")
    print("PRIORIDAD 2 CADA UNO DE SUS NIVELES")
    print(readyQueue.estrategy.priorities[2].level1)
    print(readyQueue.estrategy.priorities[2].level2)
    print(readyQueue.estrategy.priorities[2].level3)
    print("")
    print("PRIORIDAD 3 CADA UNO DE SUS NIVELES")
    print(readyQueue.estrategy.priorities[3].level1)
    print(readyQueue.estrategy.priorities[3].level2)
    print(readyQueue.estrategy.priorities[3].level3)
    print(" ")
    #print(readyQueue.getPcb())
    #print(readyQueue.getPcb())
    #print(readyQueue.getPcb())
    #print(readyQueue.getPcb())
    #print(readyQueue.getPcb())
    
    #print(mem.blocksTable)
    #print(mem.blockSize)
    #print(mem.firstBlockFree())
    #print(mem.hardDisk)
    #print(mem.memoryBlocks)
    #print(mem.spaceFreeInMemory())
main()