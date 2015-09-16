import queue
    
'''
Created on Sep 15, 2015

@author: fernando
'''

class ReadyQueue:
    def __init__(self):
        self.pcbs = queue()

    def addPcb(self, pcb):
        self.pcbs.put(pcb)

    def getPcb(self):
        return self.pcbs.get