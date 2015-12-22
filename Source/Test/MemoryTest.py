import unittest

from Code.SetUpMemoria import SetUpMemoria

class Test(unittest.TestCase):

    def setUp(self):
        self.setUpGeneral = SetUpMemoria()
        self.pcb1 = self.setUpGeneral.pcb1
        self.pcb2 = self.setUpGeneral.pcb2
        self.pcb3 = self.setUpGeneral.pcb3
        self.pcb4 = self.setUpGeneral.pcb4
        self.pcb5 = self.setUpGeneral.pcb5
        self.memory = self.setUpGeneral.mem
        self.hd = self.setUpGeneral.hd
        self.prg1 = self.setUpGeneral.prg1
        self.prg2 = self.setUpGeneral.prg2
        self.prg3 = self.setUpGeneral.prg3
        self.prg4 = self.setUpGeneral.prg4
        self.prg5 = self.setUpGeneral.prg5
        self.prg1.instructionsToPages()
        self.prg2.instructionsToPages()
        self.prg3.instructionsToPages()
        self.prg4.instructionsToPages()
        self.prg5.instructionsToPages()
        self.hd.addProgram(self.prg1)
        self.hd.addProgram(self.prg2)
        self.hd.addProgram(self.prg3)
        self.hd.addProgram(self.prg4)
        self.hd.addProgram(self.prg5)

    def test_addPCBToList(self):
        self.memory.addPCBToList(self.pcb1)
        self.memory.addPCBToList(self.pcb2)
        self.assertTrue(self.memory.pcbList.__len__() == 2)
        self.memory.addPCBToList(self.pcb2)
        self.memory.addPCBToList(self.pcb3)
        self.assertTrue(self.memory.pcbList.__len__() == 3)

    def test_getInstructionsFromDisk(self):
        list_instructions = self.memory.getInstructionsFromDisk(self.pcb1, 1)
        self.assertTrue(list_instructions.__len__() == 2)
        self.assertTrue(list_instructions[0].getMessage() == "Segunda instruccion ejecutada de CPU")
        self.assertTrue(list_instructions[1].getMessage() == "Tercera instruccion ejecutada de CPU")
   
    def test_updateOldPCBStatus(self):
        blocksTableList = self.memory.blocksTable
        self.pcb1.pagesTable.addPageToBlock(0, 1)
        self.pcb1.pagesTable.addPageToBlock(2, 3)
        self.assertTrue(self.pcb1.pagesTable.pagesToBlock[0] == (1, 0))
        self.assertTrue(self.pcb1.pagesTable.pagesToBlock[2] == (3, 0))
        
        self.memory.pcbList.append(self.pcb1)
        blocksTableList[1] = (1, 1)
        blocksTableList[3] = (3, 1)
        self.memory.updateOldPCBStatus(1)
        self.memory.updateOldPCBStatus(3)
        self.assertTrue(self.pcb1.pagesTable.pagesToBlock[0] == (1, 1))
        self.assertTrue(self.pcb1.pagesTable.pagesToBlock[2] == (3, 1))

    def test_findBlockForPage_MemoryBlocksFree(self):
        blockList = self.memory.memoryBlocks
        self.assertTrue(self.memory.findBlockForPage(1) == 0)
        blockList[0].instructionsList.append(1)
        blockList[1].instructionsList.append(4)
        blockList[2].instructionsList.append(3)
        self.assertTrue(self.memory.findBlockForPage(1) == 3)
        
    def test_findBlockForPage_MemoryFull(self):
        blockList = self.memory.memoryBlocks
        blocksTableList = self.memory.blocksTable
        
        # Asigno las paginas a los bloques
        self.pcb1.assignPageToBlock(7, 0)
        self.pcb2.assignPageToBlock(8, 1)
        self.pcb3.assignPageToBlock(9, 2)
        self.pcb4.assignPageToBlock(9, 3)
        
        # Seteo en la lista de bloques, que bloques estan mapeados a los PCBid's
        blocksTableList[0] = (0, 1)
        blocksTableList[1] = (1, 2)
        blocksTableList[2] = (2, 3)
        blocksTableList[3] = (3, 4)
        
        # Agrego los PCB's a la lista en memoria
        self.memory.pcbList.append(self.pcb1)
        self.memory.pcbList.append(self.pcb2)
        self.memory.pcbList.append(self.pcb3)
        self.memory.pcbList.append(self.pcb4)
        
        # Lleno los bloques para asegurarme que elija uno al azar
        blockList[0].instructionsList.append(1)
        blockList[1].instructionsList.append(4)
        blockList[2].instructionsList.append(3)
        blockList[3].instructionsList.append(2)
        
        self.assertTrue(self.memory.findBlockForPage(0) < 4)
        self.assertTrue(self.pcb1.pagesTable.pagesToBlock[7] == (0, 1) or self.pcb2.pagesTable.pagesToBlock[8] == (1, 1)
                        or self.pcb3.pagesTable.pagesToBlock[9] == (2, 1) or self.pcb4.pagesTable.pagesToBlock[9] == (3, 1))

    def test_MemoryFetch_WhenPCBHasNoPage(self):
        result_message = self.setUpGeneral.IOins1.getMessage()
        self.assertTrue(self.memory.fetch(self.pcb1, 1).getMessage() == result_message)
        self.assertTrue(self.pcb1.pagesTable.pagesToBlock[0] == (0, 0))
        
        result_message = self.setUpGeneral.ins2.getMessage()
        blockList = self.memory.memoryBlocks
        blockList[0].instructionsList.append(1)
        self.assertTrue(self.memory.fetch(self.pcb1, 2).getMessage() == result_message)
        self.assertTrue(self.pcb1.pagesTable.pagesToBlock[1] == (1, 0))
        self.assertTrue(self.memory.pcbList.__len__() == 1)

    def test_MemoryFetch_WhenPCBHasPageInMemory(self):
        result_message = self.setUpGeneral.IOins1.getMessage()
        self.pcb1.assignPageToBlock(0, 1)
        self.memory.saveInstruction(1, self.prg1.pages[0].instructions)
        self.assertTrue(self.memory.fetch(self.pcb1, 1).getMessage() == result_message)

    def test_MemoryFetch_WhenPCBHasPageInDisk(self):
        result_message1 = self.setUpGeneral.ins1.getMessage()
        result_message2 = self.setUpGeneral.IOins1.getMessage()
        
        self.pcb1.assignPageToBlock(0, 1)
        self.pcb2.assignPageToBlock(7, 1)
        self.pcb1.movePageToDisk(0)
        # La pagina 0 del PCB 1 esta en disco
        self.assertTrue(self.pcb1.pagesTable.pagesToBlock[0] == (1, 1))
        # La pagina 0 del PCB 2 esta en memoria
        self.assertTrue(self.pcb2.pagesTable.pagesToBlock[7] == (1, 0))

        self.memory.pcbList.append(self.pcb2)
        self.memory.blocksTable[1] = (1, 2)

        # La tabla de marcos tiene asignado el PCB 2 en el bloque 1
        self.assertTrue(self.memory.blocksTable[1] == (1, 2))
        # Hago un fetch de las instrucciones 0 y 1 del PCB 1, corroboro los resultados
        self.assertTrue(self.memory.fetch(self.pcb1, 0).getMessage() == result_message1)
        self.assertTrue(self.memory.fetch(self.pcb1, 1).getMessage() == result_message2)
        # Verifico que se actualizo la tabla de paginas de cada PCB
        self.assertTrue(self.pcb1.pagesTable.pagesToBlock[0] == (1, 0))
        self.assertTrue(self.pcb2.pagesTable.pagesToBlock[7] == (1, 1))
        # Verifico que se haya actualizado la tabla de marcos
        self.assertTrue(self.memory.blocksTable[1] == (1, 1))
        # Corroboro las instrucciones cargadas en el marco 1, que pertenezcan al PCB 1
        self.assertTrue(self.memory.memoryBlocks[1].instructionsList[0].getMessage() == result_message1)
        self.assertTrue(self.memory.memoryBlocks[1].instructionsList[1].getMessage() == result_message2)

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()