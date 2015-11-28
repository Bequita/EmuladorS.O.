from time import sleep
from threading import Thread

class Prueba(Thread):
    
    def __init__(self, message):
        Thread.__init__(self)
        self.mes = message
        
    def run(self):
        while True:
            print(self.mes)
            sleep(1)
            
thPrueba = Prueba("putazo")
thPrueba.start()