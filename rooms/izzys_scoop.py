from agent import Agent
from MaysMotors import Motor
from rooms.conners_munch import Conveyor

class Intake(Agent):
    def __init__(self, name: str, conner: Conveyor):
        super().__init__(name)
        self.motor_1 = Motor('Izzy')
        self.conner = conner

    def call(self):
        self.conner.talk()

