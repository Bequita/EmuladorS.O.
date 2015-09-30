'''
Created on 15 de set. de 2015

@author: matutee
'''

class InterruptionManager(object):

    def __init__(self):
        self.handlersList = []
        
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