'''
Created on 30 de set. de 2015

@author: matutee
'''
import unittest

from Code.SetUpMixinMaty import SetUpMixinMaty
from Code.PCB import PCB

class Test(unittest.TestCase):

    def setUp(self):
        self.suMixin = SetUpMixinMaty()
        self.pcb = PCB("first", None, None)
        self.pcb2 = PCB("second", None, None)
        self.pcb3 = PCB("third", None, None)
        self.memory = self.suMixin.mem

    def test_haveBlocks(self):
        self.assertTrue(self.memory.memoryBlocks.__len__() == 4)
        self.assertTrue(self.memory.blocksTable.__len__() == 4)
        self.assertTrue(self.memory.blocksTable[1][0] == 1)
        self.assertTrue(self.memory.blocksTable[1][1] == 0)
        self.assertTrue(self.memory.blocksTable[1][2] == None)
         
#     def test_pcbInTable(self):
#         self.assertTrue(self.memory.pcbInTable(2) == None)
# 
#     def test_refreshPositionInTable(self):
#         self.memory.refreshPositionInTable(3, 1, 1)
#         self.assertTrue(self.memory.blocksTable[1] == (1, 1, 3))
        
    def test_updatePCB(self):
        self.pcb2.assignPageToBlock(2, 6)
        self.memory.pcbList.append(self.pcb2)
        print(self.pcb2.getID())
        self.memory.updatePCB(1, 2)
        print(self.memory.pcbList[0].pagesTable.pagesToBlock[2])
        #self.assertTrue(self.memory.pcbList[0].)

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
