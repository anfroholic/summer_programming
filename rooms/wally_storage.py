from mustache.agent import Agent
from mustache.mm_motors import MM_Motor, MM_Output
from rooms.driver import Driver

class Wheels(Agent):
    def __init__(self, name: str, driver: Driver):
        super().__init__(name=name)
        self.motor_1 = MM_Motor('Mr_Louie')
        self.motor_2 = MM_Motor('Sir_Louie')
        self.motor_3 = MM_Motor('Mrs_Rodger')
        self.motor_4 = MM_Motor('Jr_Rodger')
        self.driver = driver
        self.eva = MM_Output(name='eva',
                             state=False,
                             pin=0)

    def drive(self, speed, turn) -> None:
        print(speed, turn)
        return None









