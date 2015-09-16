class IRQKind:
    KILL = "Kill"
    TIMEOUT = "TimeOut"
    NEWPCB = "NewPcb"
    IO = "IO"
    RUNTIME = "RunTime"

class IRQ:
    def __init__(self, pcb, kind):
        self.pcb = pcb
        self.tipo = kind
 
    def getPcb(self):
        return self.pcb

    def getKind(self):
        return self.kind

irq = IRQKind.KILL
print(irq)


'''
cpu ---> 
      irq = new IRQ(IRQKind.KILL, pcb) 
      im.handle(irq)


KillHandler()
IOHandler()
TimeoutHandler()


class IM():
    
    def _init_(self, ):

    def register(self, Handler):
        list.add(hanlder)
     
            
                                  
im.register(new KillHandler())
KillHandler.canHandle(int)

--------------- Setup SO -----------
im=new Interuptionmanager()
im.register(IRQKind.KILL, new KillHandler())
im.register(IRQKind.IO, new IOHandler())
--------------------------


-->  im.handle(irq (KILL, pcb))
           ---> KillHandler.handle(pcb)

-->  im.handle(irq (IO, pcb))
           ---> IOHandler.handle(pcb)

'''