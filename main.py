import pprint

def make_anon(llama):
    return lambda panda: panda * llama


double_panda = make_anon(3)

# print(f'{double_panda(12) = }')

dude = {'car': 1, 'motor': 2, 'three': 3, 'x': 102.233}

con_conner = {
    'name': 'conner',
    'burp': 14,
    'flush': .7,
    'munch': 24
}

fake_conner = {
    'name': 'connor',
    'burp': 24,
    'flush': .17,
    'munch': 29
}

izzy = 'this is a super duper extremely long string'

def house(bed):
    return f'house > {bed} < house'


def boat(wheel):
    return f'boat > {wheel} < boat'


def car(mirror):
    return f'car > {mirror} < car'


def airplane(wheel):
    return f'airplane > {wheel} < airplane'

def kachow(name, burp, **kwargs):
    print(name, burp)
    print(kwargs)

moving = [house, boat, car, airplane]

agents = ['wally', 'sally', 'conner', 'izzy', 'rhino']

if __name__ == '__main__':
    print("starting")
    kachow(0,1)
    kachow(**con_conner)





















    # print(house('key'))
    # print(boat('vroom'))
    # print(house(boat(5)))
    # for agent in agents:
    #     print(agent)
    #
    # empty = []
    #
    # for agent, move in zip(agents, moving):
    #     empty.append(move(agent))
    #
    # print(empty)
    #
    # nothing = [move(agent) for agent, move in zip(agents,moving)]
    #
    # pprint.pprint(nothing)
    #
    # print(dude)
    # pprint.pprint(dude)
