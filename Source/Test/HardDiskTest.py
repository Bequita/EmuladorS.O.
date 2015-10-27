import unittest

from Code.SetUpMixin import SetUpMixin

class HardDiskTest(unittest.TestCase):

    def setUp(self):
        self.suMixin = SetUpMixin()
        self.suMixin.hd.addProgram(self.suMixin.prg)

    def test_programAddedToHD(self):
        self.assertTrue(self.suMixin.hd.programList.__len__() == 1)

    def test_getProgramByName(self):
        programFound = self.suMixin.hd.getProgram('PrimerPrograma')
        self.assertTrue(programFound != None)
        self.assertTrue(programFound.instructionsList.__len__() == 5)

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
