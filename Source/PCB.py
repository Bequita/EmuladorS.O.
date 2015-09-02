'''
Created on 1 de set. de 2015

@author: matutee
'''

class PCB(object):

    def __init__(self, bD, pS, instructionsList):
        self.baseDirection = bD
        self.programCounter = 0
        self.programSize = pS
        self.instructions = []
        for ins in instructionsList:
            self.instructions.append(ins)
