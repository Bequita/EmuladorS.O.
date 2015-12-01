from threading import Thread, Condition

class IOManager(Thread):

    def __init__(self,handlerIO):
        Thread.__init__(self)
        self.mutexIO = Condition()
        self.listIO = []
        self.handlerIO = handlerIO
    
    def process(self):
        if(self.listIO.__len__() > 0):
            print(self.listIO)
            for irq in self.listIO:
                print("Ejecuto IOManager")
                self.handlerIO.handle(irq)
        self.removeIOFromListIO()
        
    def run(self):
        while(True):
          with self.mutexIO:
            self.mutexIO.wait()
            self.process()
    
    def removeIOFromListIO(self):
        if(self.listIO.__len__() > 0):
            for reqIO in self.listIO:
                self.listIO.remove(reqIO)
              
    def add(self,iOReq):
        self.listIO.append(iOReq)
            
            
