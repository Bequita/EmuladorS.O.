'''
Created on 29 de set. de 2015

@author: matutee
'''

from Code.PCB import PCB

class ProgramLoader(object):

    def __init__(self, hd, mem, readyQ):
        self.hardDisk = hd
        self.memory = mem
        self.readyQueue = readyQ
        
    def loadProgram(self, programName):
        program = self.hardDisk.getProgram(programName)
        programSize = program.instructionsList.__len__()
        
        self.memory.loadProgram(program)
        prPCB = PCB(self.memory.capacity.__len__() - programSize, programSize)
        self.readyQueue.addPcb(prPCB)
        