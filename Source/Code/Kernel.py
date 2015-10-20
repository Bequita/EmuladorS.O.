from ProgramLoader import ProgramLoader
from threading import Thread

class Kernel(Thread):

    def __init__(self, prLoader, intManager):
        self.programLoader = prLoader
        self.interruptionManager = intManager
        #self.scheduler = sch

    def loadProgramToPL(self, programName):
        self.programLoader.loadProgram(programName)

    def handle(self, pcb):
        # Cuando se ejecuta una interrupcion dentro de CPU
        # El scheduler le da a CPU el siguiente PCB de QReady
        self.scheduler.changePCB()
        # Me fijo el tipo de la interrrupcion
        self.interruptionManager.handle(IRQ(pcb, IRQKind."TIPO"))
