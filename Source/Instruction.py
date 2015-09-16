'''
Created on 2 de set. de 2015

@author: matutee
'''

class InstructionKind:
    IO = "IO"
    CPU = "CPU"

class Instruction(object):

    def __init__(self, msj, kind):
        self.message = msj
        self.kind= kind
        
    def printIns(self):
        print(self.message)