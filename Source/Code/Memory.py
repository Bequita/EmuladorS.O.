'''
Created on 1 de set. de 2015

@author: matutee
'''

class Memory(object):

    def __init__(self, numberOfblocks, sizeOfBlock):
        self.blockSize = sizeOfBlock
        self.memoryBlocks = self.initializeMemory(numberOfblocks)
        # Tabla de: Marco - Flag usado o no - PCB id
        self.blocksTable = self.initializeTable(numberOfblocks)
        self.pcbList = []
        
    def initializeMemory(self, blocksNumber):
        aux = 0
        totalBlocks = []
        while aux < blocksNumber:
            totalBlocks.append(Block())
            aux += 1
        
        return totalBlocks
        
    def initializeTable(self, numberOfBlocks):
        aux = 0
        table = []
        while aux < numberOfBlocks:
            table.append((aux, 0, None))
            aux += 1
        
        return table        
        
    def addInstruction(self, numberOfBlock, instruction):
        self.memoryBlocks[numberOfBlock].addInstruction(instruction)
        
# Bloque que esta en memoria            
class Block(object):
    
    def __init__(self):
        self.instructionsList = []
        
    def addInstruction(self, instruction):
        self.instructionsList.append(instruction)
        
        
    ## ESTE METODO DE MIERDA ESCRITO EN CASTELLANO LO DEJO PARA QUE VEAN QUE SE LIMPIA EL STACK DE MEMORIA
    def imprimirMemoria(self):
        for i in self.capacity:
            print(i.getMessage())
