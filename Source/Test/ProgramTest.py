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
        self.assertTrue(self.suMixin.prg.programName == 'PrimerPrograma')
        
    def test_programHasFiveInstr(self):
        self.assertTrue(self.suMixin.prg.instructionsList.__len__() == 5)

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()