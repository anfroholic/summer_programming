from agent import Agent
from mm_motors import MM_Motor, MM_Output

buttons = {'a': 1, 'b': 2, 'x': 3, 'y': 4, 'l_bum': 5, 'r_bum': 6, 'ttt': 7, 'tl': 8}
axis = {'l_stick_x': 0, 'l_stick_y': 1, 'l_trig': 2, 'r_trig': 3, 'r_stick_x': 4, 'r_stick_y': 5}
class Driver(Agent):
    def __init__(self, name: str):
        super().__init__(name=name)
        self.joy = XboxController(0)

    def get_but(self, button):
        return self.joy.getRawButton(buttons[button])

    def get_axis(self, axi):
        return self.joy.getRawAxis(axis[axi])







class XboxController:
    def __init__(self, port):
        self.port = port

    def getRawAxis(self, *args, **kwargs):
        return args, kwargs

    def getRawButton(self, *args, **kwargs):
        return args, kwargs

