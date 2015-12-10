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
    
    #iOQueue = IOQueue()
    #handlerList = []
    #ioHandler = IOHandler(iOQueue,mem)
    #handlerList.append(ioHandler)
    #timeOutHandler = TimeOutHandler()
    #handlerList.append(timeOutHandler)
    
    #scheduler = Scheduler(None,2,readyQueue)
    #programLoader = ProgramLoader(hd,mem,readyQueue)
    
    
    #iOManager = IOManager(ioHandler)
    
    #interruptionManager = InterruptionManager(so)
    #interruptionManager.handlersList.append(killHandler)
    
    #cpu = CPU(mem,interruptionManager,scheduler,iOManager)
    #kernel = Kernel(programLoader,interruptionManager,scheduler,cpu)  
    #scheduler.cpu=cpu
    
    
    #clock = Clock(cpu,iOManager)
    
    #killHandler = KillHandler(mem,kernel)
    #handlerList.append(killHandler)
    
    #mem.loadProgram(prg)
    #print(mem.capacity)
    
    #killHandler = KillHandler(mem,kernel)
    #programLoader.loadProgram("PrimerPrograma")
    
    #scheduler.start()    
    
    def printReadyQueue(readyQueue):
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
        
        
    quantum = 5
    so = None
    so = SystemComponents()#(Kernel(so),CPU(so),hd,mem,ReadyQueue(so),IOManager(so),InterruptionManager(so),IOQueue(so),
                          #quantum,ProgramLoader(so),IOHandler(so),[],Scheduler(so),TimeOutHandler(so),KillHandler(so),
                          #Clock(so))
    
    ins1 = Instruction("PRIMERA INSTRUCCION EJECUTADA DE CPU", InstructionKind.CPU)
    #IOins1 = Instruction("PRIMERA INSTRUCCION DE IO", InstructionKind.IO)
    ins2 = Instruction("SEGUNDA INSTRUCCION EJECUTADA DE CPU", InstructionKind.CPU)
    ins3 = Instruction("TERCERA INSTRUCCION EJECUTADA DE CPU", InstructionKind.CPU)
    #IOins2 = Instruction("SEGUNDA INSTRUCCION DE IO", InstructionKind.IO)
    
    listIntruction = []
    listIntruction.append(ins1)
    listIntruction.append(ins2)
    listIntruction.append(ins3)
    prg = Program("PrimerPrograma",listIntruction,3,2)    
        
    so.readyQueue = ReadyQueue(PriorityQueue())
    so.quantum = quantum
    so.hd = HardDisk()
    so.hd.addProgram(prg)
    so.mem = Memory(9,3,so.hd)
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
    

    so.programLoader = ProgramLoader(so)
    so.cpu.pcbLoaded = so.programLoader
    so.programLoader.scheduler = so.scheduler
    so.clock = Clock(so)    
    #print(so.handlerList)
    
    so.programLoader.loadProgram("PrimerPrograma")
    so.programLoader.interruptionManager = so.kernel.interruptionManager
    
    #print(mem.blocksTable)
    #print(mem.blockSize)
    #print(mem.firstBlockFree())
    #print(mem.hardDisk)
    #print(mem.memoryBlocks)
    #print(mem.spaceFreeInMemory())
    
    #so.interrupManager.executeInterruption()
    
    #print(printReadyQueue(so.readyQueue))
    #so.scheduler.assignPCB()
    so.kernel.start()
    so.iOManager.start()
    so.clock.start()
    
    #pcb1 = PCB(1,"PrimerPrograma",3,1)
    #pcb2 = PCB(2,"segundoPrograma",3,2)
    #pcb3 = PCB(3,"terceroPrograma",3,3)
    #pcb4 = PCB(4,"cuartoPrograma",3,1)
    #pcb5 = PCB(5,"quintoPrograma",3,2)
    #pcb6 = PCB(6,"sextoPrograma",3,2)
    
    #readyQueue = ReadyQueue(PriorityQueue())
    #print(s.readyQueue.getPcb())
    #readyQueue.addPcb(pcb2)
    #printReadyQueue()
    #readyQueue.addPcb(pcb5)
    #printReadyQueue()
    #readyQueue.addPcb(pcb6)
    #printReadyQueue()
    #readyQueue.addPcb(pcb4)
    #printReadyQueue()
    #readyQueue.addPcb(pcb3)
    #printReadyQueue()
    
    #print(" ")
    #print("PEDIDO DE UN PCB -----------------------------")
    #print("")
    #print(readyQueue.getPcb().__str__() + " tiene que ser el pcb que esta mas abajo en las colas")
    #print("")
    #print("COLA DE READY DESPUES DE DAR EL PCB ----------")
    #print("")
    
    #printReadyQueue()
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