'''
Created on 15 de set. de 2015

@author: matutee
'''
from Code.Kernel import Kernel

class InterruptionManager(object):

    def __init__(self,so):
        self.handlersList = so.handlerList
        self.kernel = so.kernel 
        self.irqList = []
        
    def addInterruption(self, interruption):
        self.irqList.append(interruption)
        self.kernel.modeSwitching()
    
    def executeInterruption(self):
        for interruption in self.irqList:
            self.handle(interruption)
        for interruption in self.irqList:
            self.irqList.remove(interruption)
            
    def registerHandler(self, handler):
        self.handlersList.append(handler)
        
    def handle(self, irq):
        flag = False
        for hdl in self.handlersList:
            if(hdl.canHandle(irq.getKind())):
                flag = True
                hdl.handle(irq)
        if(not flag):
            raise NameError('No existe un handler para ese tipo de instruccion')