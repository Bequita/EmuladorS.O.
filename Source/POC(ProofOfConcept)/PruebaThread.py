from time import sleep
from threading import Thread

class Prueba(Thread):
    
    def __init__(self):
        Thread.__init__(self)
        
    def run(self, message):
        while True:
            print(message)
            sleep(1)
            
thPrueba = Prueba("putazo")
thPrueba.start()