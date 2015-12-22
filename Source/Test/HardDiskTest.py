import unittest

from Code.SetUpMemoria import SetUpMemoria 

class HardDiskTest(unittest.TestCase):

    def setUp(self):
        self.suMixin = SetUpMemoria()
        self.suMixin.hd.addProgram(self.suMixin.prg1)
        self.suMixin.hd.addProgram(self.suMixin.prg2)

    def test_programAddedToHD(self):
        self.assertTrue(self.suMixin.hd.programList.__len__() == 2)

    def test_getProgramByName(self):
        programFound = self.suMixin.hd.getProgram('PrimerPrograma')
        self.assertTrue(programFound != None)
        self.assertTrue(programFound.instructionsList.__len__() == 4)

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
