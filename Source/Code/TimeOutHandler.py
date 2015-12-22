'''
Created on 15 de set. de 2015

@author: matutee
'''

from Code.Interruption import IRQKind
from Code.ReadyQueue import ReadyQueue

class TimeOutHandler(object):
    def __init__(self,sistemComponents):
        self.scheduler = sistemComponents.scheduler


    def canHandle(self, irqK):
        return irqK == IRQKind.TIMEOUT

    def handle(self, irq):
        # Hace mutex de QReady, y mete el pcb dentro de la cola
        # self.kernel.timeOutRoutine(irq)
        self.scheduler.addPCB(irq.getPcb())
        print("ANDA EL TIMEOUT HANDLER")
