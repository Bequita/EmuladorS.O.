from Code.CPU import CPU

class Clock(Thread):

    def __init__(self, cpu):
        self.CPU = cpu

    def executeClock(self):
        while(true):
            sleep(1)
            self.CPU.execute
