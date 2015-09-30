class IRQKind:
    KILL = "Kill"
    TIMEOUT = "TimeOut"
    NEWPCB = "NewPcb"
    IO = "IO"
    RUNTIME = "RunTime"

class IRQ:
    def __init__(self, PCB, kn):
        self.pcb = PCB
        self.kind = kn
 
    def getPcb(self):
        return self.pcb

    def getKind(self):
        return self.kind


