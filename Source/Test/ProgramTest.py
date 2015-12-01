'''
Created on 30 de set. de 2015

@author: matutee
'''
import unittest

from Code.SetUpMixin import SetUpMixin

class ProgramTest(unittest.TestCase):
    
    def setUp(self):
        self.suMixin = SetUpMixin()
    
    def test_programIsCalled(self):
        self.assertTrue(self.suMixin.prg1.programName == 'PrimerPrograma')
        self.assertTrue(self.suMixin.prg1.pages.__len__() == 3)
        self.suMixin.prg1.instructionsToPages()
        self.assertTrue(self.suMixin.prg1.pages[0].instructions.__len__() == 2)
        self.assertTrue(self.suMixin.prg1.pages[0].instructions[0].message == "Primera instruccion ejecutada de CPU")
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()