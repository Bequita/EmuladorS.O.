'''
Created on 15 de set. de 2015

@author: matutee
'''

from Code.Interruption import IRQKind

class TimeOutHandler(object):

    def canHandle(self, irqK):
        return irqK == IRQKind.TIMEOUT

    def handle(self, irq):
        # Hace mutex de QReady, y mete el pcb dentro de la cola
        print("ANDA EL TIMEOUT HANDLER")
