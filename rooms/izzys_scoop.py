from mustache.agent import Agent
from mustache.mm_motors import MM_Motor, MM_Output
from rooms.conners_munch import Conveyor
from rooms.driver import Driver

class Intake(Agent):
    def __init__(self, name: str, conner: Conveyor, driver: Driver):
        super().__init__(name=name)
        self.motor_1 = MM_Motor('Izzy')
        self.conner = conner
        self.light = MM_Output(name='Izzy',
                               state=False,
                               pin=1)
        self.driver = driver

    def call(self):
        self.conner.talk()

    def check(self):
        super().check()
        self.call()


