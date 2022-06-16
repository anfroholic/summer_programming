from MaysMotors import Motor

class Agent:
    def __init__(self, name, **nomnom):
        self.name = name
        m.add_agent(self)  # add self to m's list
        m.add_agent_dict(name, self)  # add self to m's dictionary

    # def __str__(self):
    #     return f"nice to meet you comrade I am {self.name}, I am a {self.__class__.__name__}"

    def check(self):
        print(f'{self.name} is working')

    def rez(self):
        print(vars(self))


class CEO:
    def __init__(self, name):
        self.name = name
        self.agents = []
        self.agents_dict = {}
        self.outputs = []

    def talk(self):
        print(f'hello i am {self.name.upper()} nice to meet you {self.agents}\n{self.agents_dict}')

    def add_agent(self, agent):
        self.agents.append(agent)

    def add_agent_dict(self, name, agent):
        self.agents_dict[name] = agent

    def check(self):
        for agent in self.agents:
            agent.check()

    def rez(self):
        for agent in self.agents:
            agent.rez()

    def find_outputs(self):
        for agent in self.agents:
            for name, value in vars(agent).items():
                print(name, value)
                if isinstance(value, Motor):
                    print(f"found {name}")
                    self.outputs.append(value)



m = CEO('m')
