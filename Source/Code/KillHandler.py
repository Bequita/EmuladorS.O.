'''
Created on 16 de set. de 2015

@author: matutee
'''

from Code.Interruption import IRQKind

class KillHandler(object):

    def __init__(self, mem, kernel):
        self.memory = mem
        self.kernel = kernel

    def canHandle(self, irqK):
        return (irqK == IRQKind.KILL)
    
    def handle(self, irq):
        self.kernel.killRoutine(irq)
        #self.memory.cleanMemoryFromPointer(irq.getPcb().baseDirection, irq.getPcb().programSize)
        
        print("Se ejecuto el KILLHANDLER")
    
        