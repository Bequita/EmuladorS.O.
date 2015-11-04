'''
Created on Sep 15, 2015

@author: fernando
'''

from queue import Queue

class ReadyQueue:
    def __init__(self):
        self.pcbs = Queue()

    def addPcb(self, pcb):
        self.pcbs.put(pcb)

    def getPcb(self):
        return self.pcbs.get
    
    

