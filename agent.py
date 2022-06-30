from mm_motors import MM_Motor, MM_Output


class Agent:
    def __init__(self, name, **nomnom):
        self.name = name
        m.add_agent(name, self)  # add self to m's dictionary

    def __str__(self):
        return f"nice to meet you comrade I am {self.name}, I am a {self.__class__.__name__}"

    def check(self):
        print(f'{self.name} is working')

    def rez(self):
        print(vars(self))


class CEO:
    def __init__(self, name):
        self.name = name
        self.agents = {}
        self.outputs_poopy = []

    def talk(self):
        print(f'hello i am {self.name.upper()} nice to meet you {self.agents}')

    def add_agent(self, name: str, agent: Agent):
        self.agents[name] = {'self': agent}
        self.agents[name].update(**{'outputs': {}})

    def check(self):
        for agent in self.agents.values():
            agent['self'].check()
            # agent.check()

    def rez(self):
        for agent in self.agents.values():
            agent['self'].rez()

    def find_outputs(self):
        outputs = (MM_Motor, MM_Output)
        for agent in self.agents.values():
            this_agent = agent["self"]
            for name, value in vars(this_agent).items():  # (name, value) = (k, v) --> (key, value)
                # print(name, value)
                if isinstance(value, outputs):
                    print(f"found {name = } and {value = }")
                    self.agents[this_agent.name]['outputs'][name] = value

    def outputs_set(self):
        for v in self.agents.values():
            outputs = v['outputs']
            for output in outputs.values():  # output --> each output
                output._set()


m = CEO('m')
