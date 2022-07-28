from mustache.agent import Agent
from mustache.mm_motors import MM_Motor, MM_Output
from rooms.driver import Driver

class Wheels(Agent):
    def __init__(self, name: str, driver: Driver, eva: dict[any], motors: list[dict[any]]):
        super().__init__(name=name)
        self.motor_1 = MM_Motor(**motors[0])
        self.motor_2 = MM_Motor(**motors[1])
        self.motor_3 = MM_Motor(**motors[2])
        self.motor_4 = MM_Motor(**motors[3])
        self.driver = driver
        self.eva = MM_Output(**eva)


    def drive(self, speed, turn) -> None:
        print(speed, turn)
        return None









