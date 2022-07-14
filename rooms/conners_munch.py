from mustache.agent import Agent
from mustache.mm_motors import MM_Motor, MM_Output
from rooms.driver import Driver


class Conveyor(Agent):
    def __init__(self, driver: Driver, burp,  **kwargs):
        super().__init__(**kwargs)
        # print(hungry)
        self.burp = burp
        self.munch = kwargs['munch']
        self.flush = kwargs['flush']
        self.motor_1 = MM_Motor('Conners motor')
        self.light = MM_Output('Conner', False, 0)
        self.state = 'sleeping'
        self.states = {"sleeping": self.sleeping, "munching": self.munching}
        self.driver = driver


    def talk(self):
        print(f'{self.burp = }\n{self.munch = }\n{self.flush = }')

    def set_motors(self):
        self.motor_1.set(self.flush)

    def test(self):
        print('testing')

    def sleeping(self):
        print('HUUUUUUuuh zzzz')

    def munching(self):
        print('nom nom nom')

    def check(self):
        self.states[self.state]()

    def __len__(self):
        return 0


