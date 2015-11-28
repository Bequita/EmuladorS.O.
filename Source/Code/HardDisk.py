'''
Created on 29 de set. de 2015

@author: matutee
'''

class HardDisk(object):

    def __init__(self):
        self.programList = []
        
    def addProgram(self, program):
        self.programList.append(program)
        
    def getProgram(self, prName):
        for item in self.programList:
            if item.programName == prName:
                return item
            