from mm_motors import MM_Motor, MM_Output

class Agent:
    def __init__(self, name, **nomnom):
        self.name = name
        m.add_agent(self)  # add self to m's list
        m.add_agent_dict(name, self)  # add self to m's dictionary

    def __str__(self):
        return f"nice to meet you comrade I am {self.name}, I am a {self.__class__.__name__}"

    def check(self):
        print(f'{self.name} is working')

    def rez(self):
        print(vars(self))


class CEO:
    def __init__(self, name):
        self.name = name
        self.agents_poopy = []
        self.agents = {}
        self.outputs = []

    def talk(self):
        print(f'hello i am {self.name.upper()} nice to meet you {self.agents_poopy}\n{self.agents}')

    def add_agent(self, agent):
        self.agents_poopy.append(agent)

    def add_agent_dict(self, name, agent):
        self.agents[name] = {'self': agent}
        self.agents[name].update(**{'outputs': []})

    def check(self):
        for agent in self.agents.values():
            agent['self'].check()
            # agent.check()

    def rez(self):
        for agent in self.agents.values():
            agent['self'].rez()

    def find_outputs(self):
        outputs = (MM_Motor, MM_Output)
        for agent in self.agents_poopy:
            for name, value in vars(agent).items():  # (name, value) = (k, v) --> (key, value)
                print(name, value)
                if isinstance(value, outputs):
                    print(f"found {name}")
                    self.outputs.append(value)
                    # self.agents_dict[agent.name] = value
                    self.agents[agent.name]['outputs'].append(value)


    def outputs_set(self):
        print(self.outputs)
        for each_output in self.outputs:
            print(each_output)
            each_output._set()





m = CEO('m')
