from abc import ABCMeta, abstractmethod

class Routine(metaclass=ABCMeta):

    def __init__(self,cpu,scheduler):
        self.cpu = cpu
    
    @abstractmethod
    def _performandRoutine(self):
        pass
    
class KillRoutine(Routine):
    def performandRoutine(self):
        self.kernel.killPCB(self.cpu.pcbLoaded)
        
class NewRoutine(Routine):
    def performandRoutine(self):
        self.kernel.newPCB(self.cpu.pcbLoaded)
        
class IORoutine(Routine):
    def performandRoutine(self):
        self.kernel.iOPCB(self.cpu.pcbLoaded)
        
class ReadyRoutine(Routine):
    def performandRoutine(self):
        self.kernel.readyPCB(self.cpu.pcbLoaded)
        
class RunningRoutine(Routine):
    def performandRoutine(self):
        self.kernel.runningPCB(self.cpu.pcbLoaded)
        
