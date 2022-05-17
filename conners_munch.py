from agent import Agent

class Conveyor(Agent):
    def __init__(self, **hungry):
        super().__init__(**hungry)
        print(hungry)
        self.burp = hungry['burp']
        self.munch = hungry['munch']
        self.flush = hungry['flush']