import unittest

from Code.SetUpMemoria import SetUpMemoria

class Test(unittest.TestCase):

    def setUp(self):
        self.setUpGeneral = SetUpMemoria()
        self.pcb1 = self.setUpGeneral.pcb1
        self.pcb2 = self.setUpGeneral.pcb2
        self.pcb3 = self.setUpGeneral.pcb3

    def test_assignPageToBlock(self):
        self.pcb1.assignPageToBlock(2, 4)
        self.assertTrue(self.pcb1.hasPageInTable(2))
        self.assertTrue(self.pcb1.pagesTable.pagesToBlock[2] == (4,0))
        self.assertTrue(self.pcb1.pcbID == 1)
        self.assertTrue(self.pcb2.pcbID == 2)
        self.assertTrue(self.pcb3.pcbID == 3)
        
    def test_pagesTable(self):
        self.pcb1.assignPageToBlock(1, 4)
        self.assertTrue(self.pcb1.pagesTable.pagesToBlock[1] == (4,0))
        self.pcb1.movePageToDisk(1)
        self.assertTrue(self.pcb1.pagesTable.pagesToBlock[1] == (4,1))
        self.pcb1.movePageToMemory(1)
        self.assertTrue(self.pcb1.pagesTable.pagesToBlock[1] == (4,0))

    def test_getBlockOfPage(self):
        self.pcb1.assignPageToBlock(5, 6)
        self.assertTrue(self.pcb1.getBlockOfPage(5) == 6)
        
    def test_obtainPageWithBlock(self):
        self.pcb2.assignPageToBlock(0, 6)
        self.pcb2.assignPageToBlock(7, 2)
        self.pcb2.assignPageToBlock(2, 3)
        self.pcb2.assignPageToBlock(5, 9)
        self.assertTrue(self.pcb2.pageCorrespondingToBlock(6) == 0)
        self.assertTrue(self.pcb2.pageCorrespondingToBlock(2) == 7)
        self.assertTrue(self.pcb2.pageCorrespondingToBlock(3) == 2)
        self.assertTrue(self.pcb2.pageCorrespondingToBlock(9) == 5)
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()