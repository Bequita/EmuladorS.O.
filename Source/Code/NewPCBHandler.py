'''
Created on Nov 27, 2015

@author: bequita
'''
from Code.Interruption import IRQKind

class NewPCBHandler(object):

    def __init__(self, sistemComponents):
        self.scheduler = sistemComponents.scheduler
        
    def canHandle(self, irqK):
        return irqK == IRQKind.NEWPCB
    
    def handle(self, irq):
        self.scheduler.addPCB(irq.getPcb())
        print("se la di al scheduler")
        