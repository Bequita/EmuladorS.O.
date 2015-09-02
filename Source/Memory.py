'''
Created on 1 de set. de 2015

@author: matutee
'''

class Memory(object):

    def __init__(self):
        self.capacity = []
        self.lastPosition = 0
        
    def loadInstructions(self, instructions, startPosition):
        start = startPosition
        for item in instructions:
            self.capacity.insert(start, item)
            self.lastPosition = self.lastPosition + 1
            start = start + 1
            # Probar si anda: lastPosition++
            
    def executeMem(self, positionMem):
        self.capacity[positionMem].printIns()