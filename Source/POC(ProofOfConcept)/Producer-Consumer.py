import threading
from threading import Thread
import time, random
from asyncio.locks import Semaphore

class Producer(Thread):
    def __init__(self,list,mutexC,mutexP, idProductor):
        Thread.__init__(self)
        self.list = list
        self.mutexP = mutexP
        self.mutexC = mutexC
        self.nombre = idProductor
    
    def run(self):
        while(True):
            self.mutexP.acquire()
            self.list.append(random.randint(0,10))
            print(self.nombre + " put an elemet, " + "list size" + self.list.__len__().__str__())
            self.mutexC.release()
            
    
class Consumer(Thread):
    def __init__(self,list,mutexC,mutexP):
        Thread.__init__(self)
        self.list = list
        self.mutexP = mutexP
        self.mutexC = mutexC
        
    def run(self):
        while(True):
            self.mutexC.acquire()
            self.list.pop()
            print("pop an elemet, " + "list size" + self.list.__len__().__str__())
            self.mutexP.release()
            
def main():
    list = []
    mutexP = threading.Semaphore(2)
    mutexC = threading.Semaphore(0)
    producer1 = Producer(list,mutexC,mutexP, "primero")
    producer2 = Producer(list,mutexC,mutexP, "segundo")
    producer3 = Producer(list,mutexC,mutexP, "tercero")
    consumidor = Consumer(list, mutexC, mutexP)
    
    
    producer1.start()
    producer2.start()
    producer3.start()
    consumidor.start()
    
main()            
        
            
        