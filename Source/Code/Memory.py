from _random import Random
class Memory(object):

    def __init__(self, numberOfblocks, sizeOfBlock,hardDisk):
        self.hardDisk = hardDisk
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
    
    def pcbInTable(self, numberBlock):
        tupleAux = self.blocksTable[numberBlock]
        return tupleAux[2]
    
    def refreshPositionInTable(self, pcbID, numberBlock, status):
        self.blocksTable[numberBlock] = (numberBlock, status, pcbID)
        
    def updatePCB(self, pcbId, page):
        for item in self.pcbList:
            if(item.getID() == pcbId):
                item.movePageToDisk(page)
    
    def saveInstruction(self,numberBlock,instBlock):
        block = self.memoryBlocks[numberBlock]
        block.instructionsList.insert(0, instBlock)
        
    def spaceFreeInMemory(self):
        for item in self.memoryBlocks:
            if(item.isEmpty()):
                return True
        return False
    
    def firstBlockFree(self):
        aux = -1
        for item in self.memoryBlocks:
            aux += 1
            if(item.isEmpty()):
                return aux
                      
    def addInstruction(self, numberOfBlock, instruction):
        self.memoryBlocks[numberOfBlock].addInstruction(instruction)
        
    def loadInstructionsToMemory(self, pcb, page):
        #traigo el programa de disco
        program = self.hardDisk.getProgram(pcb.programName)
        #asumo que el largo de las paginas del programa es igual a la de memoria
        instBlock = program.getPage(page).instructionsList #========> HAY QUE HACERLO. VIC PUTO.
        # Me traigo el pcb y seteo que las instrucciones de la pagina correspondiente al bloque estan en disco
        idPcbOutgoing = self.pcbInTable(pcb.getBlockOfPage(page))
        self.updatePCB(idPcbOutgoing,page)
        #inserto las instruciones en la posicion indicada
        self.saveInstruction(pcb.getBlockOfPage(page), instBlock)
        #actualizo estado de tabla
        self.refreshPositionInTable(pcb.getID(),pcb.getBlockOfPage(page),1)
        
    def changePCBPageFromDiskToMemory(self, pcb, page):
        #actualizo estado pcb
        pcb.movePageToMemory(page)
        
    def assingBlockToInstructions(self,pcb):
        #traigo el programa de disco
        program = self.hardDisk.getProgram(pcb.programName)
        
        if(self.spaceFreeInMemory()):
            #guardo instruciones en memoria
            block = self.firstBlockFree
            instBlock = program.getPage(block).instructionsList
            self.saveInstruction(block,instBlock)
        else:
            block = Random.randint(0, self.memoryBlocks.__len__())
            #actualizo PCB saliente
            idPcbOutgoing = self.pcbInTable(block)
            self.updatePCB(idPcbOutgoing,block)
            #inserto las instruciones en la posicion indicada
            self.saveInstruction(block, instBlock)
            #actualizo estado de tabla
            self.refreshPositionInTable(pcb.getID(),block,1)
                    
    def fetch(self, pcb, instruction):
        self.addPCBToList(pcb)
        tupleResult = divmod(instruction, self.blockSize)
        page = tupleResult[0]
        instPosition = tupleResult[1]
        
        # Caso 1: el pcb tiene un marco asociado a la pagina
        if pcb.hasPageInTable(page):
            # Corroboro si esta en memoria las instrucciones de la pagina
            if (not pcb.movePageToDisk(page)):
                block = self.memoryBlocks[pcb.getBlockOfPage(page)]
                return block.getInstruction(instPosition)   
            else:
                # ir a disco y cargar la pagina a memoria
                self.loadInstructionsToMemory(pcb, page)
                # decirle al pcb que las instrucciones de esa pagina estan en memoria ahora
                self.changePCBPageFromDiskToMemory(pcb, page)
                # bloque donde estan las instrucciones a buscar
                block = self.memoryBlocks[pcb.getBlockOfPage(page)]
                # retornar la instruccion correspondiente
                return block.getInstruction(instPosition)
        else:
            #ir a disco,cargar la pagina a memoria,actualizar pcb saliente,retornar numero de bloque
            self.assingBlockToInstructions(pcb)
            # bloque donde estan las instrucciones a buscar
            block = self.memoryBlocks[pcb.getBlockOfPage(page)]
            # asignar pagina y bloque al pcb
            pcb.assignPageToBlock(page,block)
            # retornar la instruccion correspondiente
            return block.getInstruction(instPosition)
    
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
    
    def isEmpty(self):
        return self.instructionsList.__len__() > 0
        
