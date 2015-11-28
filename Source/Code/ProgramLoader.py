from Code.PCB import PCB
from Code.Interruption import IRQ, IRQKind

class ProgramLoader(object):

    def __init__(self, hd, mem, interrupManager):
        self.hardDisk = hd
        self.memory = mem
        self.interruptionManager = interrupManager

    def loadProgram(self, programName):
        programFromDisk = self.hardDisk.getProgram(programName)
        programSize = programFromDisk.instructionsList.__len__()
        priority = programFromDisk.priority
        
        pcbNew = PCB(programName, programSize, priority)
        self.interruptionManager.handle(IRQ(pcbNew, IRQKind.NEWPCB))
