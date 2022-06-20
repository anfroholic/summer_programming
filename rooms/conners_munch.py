from agent import Agent
from mm_motors import MM_Motor, MM_Output


class Conveyor(Agent):
    def __init__(self, **hungry):
        super().__init__(**hungry)
        # print(hungry)
        self.burp = hungry['burp']
        self.munch = hungry['munch']
        self.flush = hungry['flush']
        self.motor_1 = MM_Motor('Conners motor')
        self.light = MM_Output('Conner', False, 0)

    def talk(self):
        print(f'{self.burp = }\n{self.munch = }\n{self.flush = }')

    def set_motors(self):
        self.motor_1.set(self.flush)
        self.motor_1._set(self.flush)

    def test(self):
        print('testing')



