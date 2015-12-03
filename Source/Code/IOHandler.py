'''
Created on 16 de set. de 2015

@author: matutee
'''

from Code.Interruption import IRQKind

class IOHandler(object):

    def __init__(self, systemComponents):
        self.iOQueue = systemComponents.iOQueue
        self.memory = systemComponents.mem

    def canHandle(self, irqK):
        return (irqK == IRQKind.IO)

    def handle(self, irq):
        inst = self.fetch(irq.getPcb())
        self.iOQueue.addInstructionToIOQueue(inst)
        
    def fetch(self, pcb):
        return self.memory.fetchMem(pcb.baseDirection + pcb.programCounter -1)
