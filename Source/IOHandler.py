'''
Created on 16 de set. de 2015

@author: matutee
'''

from Interruption import IRQKind

class IOHandler(object):

    def __init__(self, ioQ, mem):
        self.IOQueue = ioQ
        self.memory = mem

    def canHandle(self, irqK):
        return (irqK == IRQKind.IO)
    
    def handle(self, irq):
        IOInstruction = self.fetch(irq.getPcb())
        self.IOQueue.addInstructionToIOQueue(IOInstruction)
        print("El IOHANDLER agrega una instruccion a la cola de IO")
        
    def fetch(self, pcb):
        return self.memory.fetchMem(pcb.baseDirection + pcb.programCounter)