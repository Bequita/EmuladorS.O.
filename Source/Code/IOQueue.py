'''
Created on 16 de set. de 2015

@author: matutee
'''

class IOQueue(object):

    def __init__(self):
        self.IOQueue = []
        
    def addInstructionToIOQueue(self, inst):
        self.IOQueue.append(inst)
        
    def getQueue(self):
        return self.IOQueue
