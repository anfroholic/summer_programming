from agent import Agent
from MaysMotors import Motor

class Conveyor(Agent):
    def __init__(self, **hungry):
        super().__init__(**hungry)
        print(hungry)
        self.burp = hungry['burp']
        self.munch = hungry['munch']
        self.flush = hungry['flush']
        self.motor_1 = Motor('Conner')

    def talk(self):
        print(f'{self.burp = }\n{self.munch = }\n{self.flush = }')

    def set_motors(self):
        self.motor_1.set(self.flush)
