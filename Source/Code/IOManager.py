from threading import Thread, Condition

class IOManager(Thread):

    def __init__(self,so):
        Thread.__init__(self)
        self.mutexIO = Condition()
        self.listIO = []
        self.handlerIO = so.handlerIO
    
    def process(self):
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
        for reqIO in self.listIO:
            self.listIO.remove(reqIO)
              
    def add(self,iOReq):
        self.listIO.append(iOReq)
            
            
