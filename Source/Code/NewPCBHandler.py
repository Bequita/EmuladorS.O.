'''
Created on Nov 27, 2015

@author: bequita
'''
from Code.Interruption import IRQKind

class NewPCBHandler(object):

    def __init__(self, readyQ):
        self.readyQueue = readyQ
        
    def canHandle(self, irqK):
        return irqK == IRQKind.NEWPCB
    
    def handle(self, irq):
        self.readyQueue.addPcb(irq.getPcb())
        