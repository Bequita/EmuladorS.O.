from threading import Thread
from time import sleep

class Prueba(Thread):
    
    def __init__(self):
        Thread.__init__(self)

    def run(self):
        while True:
            print("Pablito, te haces querer")
            sleep(1)
            
thPrueba = Prueba()
thPrueba.start()