'''
Created on 1 de set. de 2015

@author: matutee
'''

class PCB(object):

    Id = 0

    def __init__(self, prName, pS, prio):
        self.pcbID = PCB.Id
        self.incrementId()
        self.programName = prName
        self.pagesTable = PagesTable()
        self.programSize = pS
        self.nextInstruction = 0
        self.priority = prio
        
    def incrementId(self):
        PCB.Id += 1
        
    def assignPageToBlock(self, page, block):
        self.pagesTable.pageToBlock(page, block)
        
class PagesTable(object):
    
    def __init__(self):
        self.pagesToBlock = {}
        
    def pageToBlock(self, page, block):
        self.pagesToBlock[page] = (block, 0)
        
    def isNowInDisc(self, page, block):
        self.pagesToBlock[page] = (block, 1)