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
        
    def fetch(self, pcb, instruction):
        self.addPCBToList(pcb)
        
        tupleResult = divmod(instruction, self.blockSize)
        page = tupleResult[0]
        instPosition = tupleResult[1]
        
        # Caso 1: el pcb tiene un marco asociado a la pagina, y la misma esta en memoria
        if pcb.hasPageInTable(page):
            block = self.memoryBlocks[pcb.getBlockOfPage(page)]
            
            # Corroboro si esta en memoria las instrucciones de la pagina
            if (not pcb.isPageInDisk(page)):
                return block.getInstruction(instPosition)
            # Voy a buscar las instrucciones al disco y las cargo a memoria   
            else:
                # ir a disco y cargar la pagina a memoria
                self.loadInstructionsToMemory(pcb.programName, page, block)
                # decirle al pcb que las instrucciones de esa pagina estan en memoria ahora
                self.changePCBPageFromDiskToMemory(pcb, page)
                # retornar la instruccion correspondiente
                return block.getInstruction(instPosition)
                
        else:
        #FALTA UNA CONDICION MAS
        
        
    
    def addPCBToList(self, pcb):
        exist = False
        for item in self.pcbList:
            if item.pcbID == pcb.pcbID:
                exist = True
                
        if not exist:
            self.pcbList.append(pcb)
        
        
# Bloque que esta en memoria            
class Block(object):
    
    def __init__(self):
        self.instructionsList = []
        
    def addInstruction(self, instruction):
        self.instructionsList.append(instruction)
     
    def getInstruction(self, instPosition):
        return self.instructionsList[instPosition]
        
            
            
            
            
        
        
        
        
        
        
        