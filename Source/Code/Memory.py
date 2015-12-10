import random

class Memory(object):

    def __init__(self, numberOfblocks, sizeOfBlock, hd):
        self.hardDisk = hd
        self.blockSize = sizeOfBlock
        self.memoryBlocks = self.initializeMemory(numberOfblocks)
        # Tabla de: (Marco, idPCB)
        self.blocksTable = self.initializeTable(numberOfblocks) 
        self.pcbList = []
        self.lastIdPcbAssing = None

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
            table.append((aux, None))
            aux += 1
        return table

    def pcbInTable(self, numberBlock):
        tupleAux = self.blocksTable[numberBlock]
        return tupleAux[1]
    
    def getPCB(self, idPCB):
        for item in self.pcbList:
            if item.pcbID == idPCB:
                return item
  
    def saveInstruction(self, numberBlock, instBlock):
        block = self.memoryBlocks[numberBlock]
        block.clean()
        for item in instBlock:
            block.addInstruction(item)

    def firstBlockFree(self):
        aux = -1
        for item in self.memoryBlocks:
            aux += 1
            if(item.isEmptyBlock()):
                return aux
            
        return -1
    
    def getInstructionsFromDisk(self, pcb, pageNumber):
        program = self.hardDisk.getProgram(pcb.programName)
        instructionList = program.getPage(pageNumber).instructions
        
        return instructionList
    
    def findBlockForPage(self, page):
        blockNumber = self.firstBlockFree()
        
        if blockNumber == -1:
            blockNumber = random.randrange(self.memoryBlocks.__len__()-1)
            self.updateOldPCBStatus(blockNumber)
            
        return blockNumber
    
    def updateOldPCBStatus(self, blockNumber):
        idPCB = self.pcbInTable(blockNumber)
        oldPCB = self.getPCB(idPCB)
        oldPCB.movePageToDisk(oldPCB.pageCorrespondingToBlock(blockNumber))
        
    def updateBlocksTable(self, blockNumber, idpcb):
        self.blocksTable[blockNumber] = (blockNumber, idpcb)
        
    def addPCBToList(self, pcb):
        exist = False
        for item in self.pcbList:
            if item.pcbID == pcb.pcbID:
                exist = True
                
        if not exist:
            self.pcbList.append(pcb)
                    
    def fetch(self, pcb, instruction):
        self.addPCBToList(pcb)
        tupleResult = divmod(instruction, self.blockSize)
        page = tupleResult[0]
        instPosition = tupleResult[1]
        
        if pcb.hasPageInTable(page):
            # Corroboro si esta en memoria las instrucciones de la pagina
            if (not pcb.inHardDisk(page)):
                block = self.memoryBlocks[pcb.getBlockOfPage(page)]
                return block.getInstruction(instPosition)
            else:
                current_block = pcb.getBlockOfPage(page)
                # Buscar en disco las instrucciones a cargar
                instructionsList = self.getInstructionsFromDisk(pcb, page)
                # Actualizar el PCB que estaba ocupando ese marco
                self.updateOldPCBStatus(current_block)
                # Cargar las instrucciones en memoria
                self.saveInstruction(pcb.getBlockOfPage(page), instructionsList)
                # Decirle al pcb nuevo que la pagina esta ahora en memoria
                pcb.movePageToMemory(page)
                # Actualizo la tabla de marcos
                self.updateBlocksTable(current_block, pcb.pcbID)
                # Retornar las instrucciones
                block = self.memoryBlocks[pcb.getBlockOfPage(page)]
                return block.getInstruction(instPosition)
        else:
            # Buscar en disco las instrucciones a cargar
            instructionsList = self.getInstructionsFromDisk(pcb, page)
            # Encontrar un marco libre en la tabla de marcos para asignarle la pagina (actualizar pcb saliente)
            freeBlockNumber = self.findBlockForPage(page)
            # Asignar pagina -> marco dentro del pcb
            pcb.assignPageToBlock(page, freeBlockNumber)
            # Cargar las instrucciones a memoria
            self.saveInstruction(freeBlockNumber, instructionsList)
            # Actualizo la tabla de marcos
            self.updateBlocksTable(freeBlockNumber, pcb.pcbID)
            # Retorno la instruccion correspondiente
            block = self.memoryBlocks[pcb.getBlockOfPage(page)]
            return block.getInstruction(instPosition)
        

class Block(object):
    
    ''' 
        Clase Bloque que esta en memoria 
    '''
    
    def __init__(self):
        self.instructionsList = []
        
    def addInstruction(self,instruction):
        self.instructionsList.append(instruction)
     
    def getInstruction(self, instPosition):
        print("lista de instrucciones" + self.instructionsList.__str__())
        return self.instructionsList[instPosition]
    
    def isEmptyBlock(self):
        return self.instructionsList.__len__() == 0
    
    def clean(self):
        self.instructionsList = []
     
