'''
Created on 15 de set. de 2015

@author: matutee
'''

from Interruption import IRQKind

class TimeOutHandler(object):

    def canHandle(self, irqK):
        return irqK == IRQKind.TIMEOUT
    
    def handle(self, irq):
        print("ANDA EL TIMEOUT HANDLER")
    