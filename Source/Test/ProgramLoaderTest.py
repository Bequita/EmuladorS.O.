'''
Created on Nov 27, 2015

@author: bequita
'''
import unittest

from Code.SetUpMixinMaty import SetUpMixinMaty

class Test(unittest.TestCase):

    def setUp(self):
        self.suMixin = SetUpMixinMaty()
        self.suMixin.hd.addProgram(self.suMixin.prg1)
        self.suMixin.hd.addProgram(self.suMixin.prg2)
        self.programLoader = self.suMixin.prLoader

    def test_PcbSuccessfullyCreated(self):
        self.programLoader.loadProgram("PrimerPrograma")
        self.pcb = self.suMixin.readyQueue.getPcb()
        self.assertTrue(self.pcb.programName == "PrimerPrograma")
        self.assertTrue(self.pcb.pcbID == 0)
        self.assertTrue(self.pcb.priority == 1)


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()