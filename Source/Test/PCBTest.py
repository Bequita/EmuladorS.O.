import unittest

from Code.SetUpMixinMaty import SetUpMixinMaty

class Test(unittest.TestCase):

    def setUp(self):
        self.setUpGeneral = SetUpMixinMaty()
        self.pcb = self.setUpGeneral.pcb
        self.pcb2 = self.setUpGeneral.pcb2
        self.pcb3 = self.setUpGeneral.pcb3

    def test_assignPageToBlock(self):
        self.pcb.assignPageToBlock(2, 4)
        self.assertTrue(self.pcb.hasPageInTable(2))
        self.assertTrue(self.pcb.pagesTable.pagesToBlock[2] == (4,0))
        self.assertTrue(self.pcb.pcbID == 1)
        self.assertTrue(self.pcb2.pcbID == 2)
        self.assertTrue(self.pcb3.pcbID == 3)
        
    def test_pagesTable(self):
        self.pcb.assignPageToBlock(1, 4)
        self.assertTrue(self.pcb.pagesTable.pagesToBlock[1] == (4,0))
        self.pcb.movePageToDisk(1)
        self.assertTrue(self.pcb.pagesTable.pagesToBlock[1] == (4,1))
        self.pcb.movePageToMemory(1)
        self.assertTrue(self.pcb.pagesTable.pagesToBlock[1] == (4,0))

    def test_getBlockOfPage(self):
        self.pcb.assignPageToBlock(5, 6)
        self.assertTrue(self.pcb.getBlockOfPage(5) == 6)
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()