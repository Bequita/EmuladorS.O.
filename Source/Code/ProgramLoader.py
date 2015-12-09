from Code.PCB import PCB
from Code.Interruption import IRQ, IRQKind

class ProgramLoader(object):

    def __init__(self, systemComponents):
        self.hardDisk = systemComponents.hd
        self.memory = systemComponents.mem
        self.interruptionManager = systemComponents.interrupManager
        self.scheduler = systemComponents.scheduler

    def loadProgram(self, programName):
        program = self.hardDisk.getProgram(programName)
        programSize = program.instructionsList.__len__()
        #generar random 1...3 para la prioridad o poner una cualquiera
        #self.memory.loadProgram(program)
        #prPCB = PCB(self.memory.capacity.__len__() - programSize, programSize,2)
        #self.scheduler.addPCB(prPCB)
        
        pcbNew = PCB(programName, programSize, 2)
        self.interruptionManager.handle(IRQ(pcbNew, IRQKind.NEWPCB))
