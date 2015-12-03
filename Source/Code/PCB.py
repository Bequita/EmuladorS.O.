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
        
    def getID(self):
        return self.pcbID
     
    #
    def assignPageToBlock(self, page, block):
        self.pagesTable.addPageToBlock(page, block)
        
    #    
    def movePageToDisk(self, page):
        self.pagesTable.moveToDisk(page)
    
    #   
    def movePageToMemory(self, page):
        self.pagesTable.moveToMemory(page)
    
    #    
    def hasPageInTable(self, page):
        return self.pagesTable.pagesToBlock.get(page) != None
    
    #
    def getBlockOfPage(self, page):
        return self.pagesTable.getBlock(page)

class PagesTable(object):
    
    def __init__(self):
        self.pagesToBlock = {}
        
    def addPageToBlock(self, page, block):
        self.pagesToBlock[page] = (block, 0)
        
    def moveToDisk(self, page):
        tuplePage = self.pagesToBlock[page]
        self.pagesToBlock[page] = (tuplePage[0], 1)
        
    def moveToMemory(self, page):
        tuplePage = self.pagesToBlock[page]
        self.pagesToBlock[page] = (tuplePage[0], 0)
        
    def getBlock(self, page):
        tuplePage = self.pagesToBlock[page]
        return tuplePage[0]
    
    def getNumberBlock(self,page):
        tuplePage = self.pagesToBlock[page]
        return tuplePage[0]
    