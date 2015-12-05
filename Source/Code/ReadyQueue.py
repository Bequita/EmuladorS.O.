'''
Created on Sep 15, 2015

@author: fernando
'''
import Queue

class ReadyQueue:
    def __init__(self, estrategy):
        self.estrategy = estrategy
    
    def addPcb(self, pcb):
        self.estrategy.addPcb(pcb)

    def getPcb(self):
        return self.estrategy.getPcb()

class Cell:
    def __init__(self):
        self.level1 = []
        self.level2 = []
        self.level3 = []       
        
    def addPcb(self, pcb):
        self.level1.insert(0, pcb)

    def returnLastLevel(self):
        return (self.level3)
    
    def ageFirst(self):
        self.level3=self.level2
        self.level2 = []
        self.level2 = (self.level1)
        self.level1 = []        

    def age(self, level):
        self.level3 = []
        self.level3 = self.level2
        self.level2 = []
        self.level2 = self.level1
        self.level1 = []
        self.level1 = level

    def ageLast(self, level):
        # self.level3 = [] #los elementos de este nivel solo salen con un getPcb()
        self.level3 = self.level2
        self.level2 = []
        self.level2 = self.level1
        self.level1 = []
        self.level1 = level

    def getPcb(self):
        if (self.level3.__len__() != 0):
            pcb = (self.level3.pop())
        elif(self.level2.__len__() != 0):
            pcb = (self.level2.pop())
        else: pcb = (self.level1.pop())
        return pcb
    ''' Siempre va a sacar un elemento en una celda que tiene elementos,
        La logica del filtrado la realiza la cola al momento de 
        hacer el llamado al metodo devolver '''

    def empty(self):
        return (len(self.level3) == 0 and len(self.level2) == 0 and len(self.level1) == 0)
    
    def returnLevel(self, level):
        if (level == 1):
            return (self.level1)
        if(level == 2):
            return (self.level2)
        if(level == 3):
            return (self.level3)

class PriorityQueue:
    def __init__(self):
        self.priorities = {}
        self.numOfPriorities = 3
        self.priorities[1] = Cell()
        self.priorities[2] = Cell()
        self.priorities[3] = Cell()

    def addPcb(self, pcb):
        addTo = pcb.priority
        self.envejecer()
        self.priorities[addTo].addPcb(pcb)

    def envejecer(self):
        lastLevel2 = self.priorities[2].returnLastLevel()
        lastLevel1 = self.priorities[1].returnLastLevel()
        self.priorities[3].ageLast(lastLevel2)
        self.priorities[2].age(lastLevel1)
        self.priorities[1].ageFirst()
        
    def empty(self):
        return (self.priorities[1].empty() and
                self.priorities[2].empty() and 
                self.priorities[3].empty())
                
    
    def getPcb(self):
        priority = self.numOfPriorities # para buscar en todas las prioridades
        priorityLevel = self.numOfPriorities # para buscar en todos los niveles de un prioridad determinada
        found = False 
        pcb = None
        while(priority > 0 and found == False): # busca en cada prioridad
            if(not self.priorities[priority].empty()):
                priorityLevel = self.numOfPriorities
                while(priorityLevel > 0 and found == False): # busca en cada nivel de la prioridad
                    if(not (self.priorities[priority]).empty()):
                        found = True
                        pcb = (self.priorities[priority]).getPcb()
                    else:
                        priorityLevel = priorityLevel - 1 
            priority = priority - 1
        return(pcb)                
                
class FifoQueue:
    def __init__(self):
        self.queue = Queue()

    def addPcb(self, pcb):
        self.queue.put(pcb)

    def getPcb(self):
        return self.queue.get()

    def size(self):
        return self.queue.qsize          
