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

    def fetchMem(self, position):
        return self.capacity[position]
    
    def cleanMemoryFromPointer(self, start, length):
        while(start < length):
            self.capacity[start] = None
            start = start + 1
            
    ## ESTE METODO DE MIERDA ESCRITO EN CASTELLANO LO DEJO PARA QUE VEAN QUE SE LIMPIA EL STACK DE MEMORIA
    def imprimirMemoria(self):
        for i in self.capacity:
            print(i)