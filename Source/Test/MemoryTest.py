'''
Created on 30 de set. de 2015

@author: matutee
'''
import unittest

from Code.SetUpMixin import SetUpMixin
from Code.Instruction import InstructionKind

class Test(unittest.TestCase):

    def setUp(self):
        self.suMixin = SetUpMixin()
        self.suMixin.mem.loadProgram(self.suMixin.prg)

    def test_loadProgramInMemory(self):
        self.assertTrue(self.suMixin.mem.capacity.__len__() == 5)
        self.assertTrue(self.suMixin.mem.lastPosition == 5)
    
    def test_fetchMem(self):
        self.instCPU = self.suMixin.mem.fetchMem(2)
        self.instIO = self.suMixin.mem.fetchMem(4)
        self.assertTrue(self.instCPU.kind == InstructionKind.CPU)
        self.assertTrue(self.instCPU.message == 'Segunda instruccion ejecutada de CPU')
        self.assertTrue(self.instIO.kind == InstructionKind.IO)
        self.assertTrue(self.instIO.message == 'SEGUNDA INSTRUCCION DE IO')

    def test_cleanMemoryFromPointer(self):
        self.suMixin.mem.cleanMemoryFromPointer(2, 3)
        instOcurrences = 0
        for ins in self.suMixin.mem.capacity:
            if ins != None:
                instOcurrences = instOcurrences + 1
        self.assertTrue(instOcurrences == 2)

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()