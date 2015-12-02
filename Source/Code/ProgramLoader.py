from Code.PCB import PCB
from Code.Interruption import IRQ, IRQKind

class ProgramLoader(object):

    def __init__(self, hd, mem, interrupManager):
        self.hardDisk = hd
        self.memory = mem
        self.interruptionManager = interrupManager

    def loadProgram(self, programName):
        program = self.hardDisk.getProgram(programName)
        programSize = program.instructionsList.__len__()

        self.memory.loadProgram(program)
        prPCB = PCB(self.memory.capacity.__len__() - programSize, programSize,2)
        self.readyQueue.addPcb(prPCB)
        
        pcbNew = PCB(programName, programSize, priority)
        self.interruptionManager.handle(IRQ(pcbNew, IRQKind.NEWPCB))
