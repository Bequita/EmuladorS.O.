'''
Created on 2 de set. de 2015

@author: matutee
'''

class Instruction(object):

    def __init__(self, msj):
        self.message = msj
        
    def printIns(self):
        print(self.message)