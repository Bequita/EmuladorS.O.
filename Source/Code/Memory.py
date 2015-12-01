'''
Created on 1 de set. de 2015

@author: matutee
'''

class Memory(object):

    def __init__(self):
        self.capacity = []
        self.lastPosition = 0
        
    def loadProgram(self, program):
        self.loadInstructions(program.instructionsList)
        
    def loadInstructions(self, instructions):
        for item in instructions:
            self.capacity.insert(self.lastPosition, item)
            self.lastPosition = self.lastPosition + 1

    def fetchMem(self, position):
        return self.capacity[position]
    
    def cleanMemoryFromPointer(self, start, length):
        while(length > 0):
            self.capacity[start] = None
            start = start + 1
            length = length - 1
            
    ## ESTE METODO DE MIERDA ESCRITO EN CASTELLANO LO DEJO PARA QUE VEAN QUE SE LIMPIA EL STACK DE MEMORIA
    def imprimirMemoria(self):
        for i in self.capacity:
            print(i.getMessage())