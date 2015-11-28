'''
Created on 15 de set. de 2015

@author: matutee
'''

from Code.Interruption import IRQKind
from Code.ReadyQueue import ReadyQueue

class TimeOutHandler(object):

    def canHandle(self, irqK):
        return irqK == IRQKind.TIMEOUT

    def handle(self, irq):
        # Hace mutex de QReady, y mete el pcb dentro de la cola
        ReadyQueue.addPcb(self,irq.getPcb())
        print("ANDA EL TIMEOUT HANDLER")
