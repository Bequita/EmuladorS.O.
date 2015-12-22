
import unittest

from Code.SetUpMemoria import SetUpMemoria

class ProgramTest(unittest.TestCase):
    
    def setUp(self):
        self.setUpGeneral = SetUpMemoria()
    
    def test_programIsCalled(self):
        self.assertTrue(self.setUpGeneral.prg1.programName == 'PrimerPrograma')
        self.assertTrue(self.setUpGeneral.prg1.pages.__len__() == 2)
        self.setUpGeneral.prg1.instructionsToPages()
        self.assertTrue(self.setUpGeneral.prg1.pages[0].instructions.__len__() == 2)
        self.assertTrue(self.setUpGeneral.prg1.pages[0].instructions[0].message == "Primera instruccion ejecutada de CPU")
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()