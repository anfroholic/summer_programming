from mustache.agent import Agent
from mustache.mm_motors import MM_Motor, MM_Output
from rooms.driver import Driver
from mustache.auto import Autonomous

class Conveyor(Agent):
    def __init__(self, driver: Driver, **kwargs):
        super().__init__(**kwargs)
        # print(hungry)
        self.munch = kwargs['munch']
        self.flush = kwargs['flush']
        self.motor_1 = MM_Motor('Conners motor')
        self.line_sens = MM_Output('Conner', False, 0)
        self.state = 'sleeping'
        self.states = {"sleeping": self.sleeping, "munching": self.munching, "burping": self.burping}
        self.driver = driver
        self.archie = Autonomous(name='conner')


    def burp(self):
        """
        bring the cargo backwards: setting the motors in reverse  *
        where is the motor(s) position *
        x amount: encoders tic position
        stop motors
        """
        x = 5
        routine = [
            lambda: self.set_motors(speed=-.8),
            lambda: self.motor_1.reset_encoder(),
            lambda: self.motor_1.get_pos() > 5,
            lambda: self.set_motors(speed=0),
            lambda: self.sleep()
        ]
        self.state = "burping"
        self.archie.run(routine)

    def talk(self):
        print(f'{self.burp = }\n{self.munch = }\n{self.flush = }')

    def set_motors(self, speed):
        self.motor_1.set(speed)

    def test(self):
        print('testing')

    def sleeping(self):
        """
        see if cargo hits line sens. -> munch

        """
        print('HUUUUUUuuh zzzz')

    def munch(self):
        """
        move cargo until line sens no see
        """
        self.set_motors(speed=.4)
        self.state = 'munching'

    def munching(self):
        if not self.line_sens.state:
            self.set_motors(speed=0)
            self.sleep()
        print('nom nom nom')

    def burping(self):
        self.archie.check()  # checking archies func

    def check(self):
        self.states[self.state]()
        return None

    def __len__(self):
        return 0

    def sleep(self):
        self.state = "sleeping"

    def whisper(self, msg):
        # {'from': 'agent', 'msg': 'the message'}
        print(f'doing {msg} right now')
        if msg['from'] == 'izzy':
            if msg['msg'] == 'sleep':
                self.sleep()
                print('I got my pjs on')
            elif msg['msg'] == 'burp':
                self.burp()
                print('better get a napkin')