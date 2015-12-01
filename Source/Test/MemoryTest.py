'''
Created on 30 de set. de 2015

@author: matutee
'''
import unittest

from Code.SetUpMixin import SetUpMixin

class Test(unittest.TestCase):

    def setUp(self):
        self.suMixin = SetUpMixin()
        self.memory = self.suMixin.mem

    def test_haveBlocks(self):
        self.assertTrue(self.memory.memoryBlocks.__len__() == 4)
        self.assertTrue(self.memory.blocksTable.__len__() == 4)
        self.assertTrue(self.memory.blocksTable[1][0] == 1)      
        self.assertTrue(self.memory.blocksTable[1][1] == 0)
        self.assertTrue(self.memory.blocksTable[1][2] == None)

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
