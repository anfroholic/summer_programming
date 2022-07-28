from rooms.conners_munch import Conveyor
from rooms.izzys_scoop import Intake
import config
from mustache.agent import m
from rooms.driver import Driver
from rooms.wally_storage import Wheels
from mustache.auto import Autonomous
from pprint import pprint
'''
Inheritance  IS_A
Agent --> Conner  

Agregation   NEEDS_A WANTS_A
conner --> izzy 
needy conner --> wants izzy

Composition  HAS_A
conner --> motor_1
'''

buttons = ["a", "b", "x", "y", "l_bum", "r_bum", "ttt", "tl"]

# an agency is born
driver = Driver(name='driver')
fake_conner = Conveyor(driver=driver, **config.fake_conner)
conner = Conveyor(driver=driver, **config.con_conner)
izzy = Intake(conner=conner, driver=driver, **config.izzy)
wally = Wheels(driver=driver, **config.wally)


timmy = 4


def print_it():
    print('it')


it = lambda: 4 > 58

"""
lambdas

truth table 
None: next
True: next
False: wait
"""


ta = [
    # dict(cmd=print_it),
    # lambda: print('it'),
    lambda: wally.drive(speed=.5, turn=.5),
    lambda: izzy.motor_1.set(speed=.5),
    lambda: izzy.motor_1.set(speed=0),
    print_it,
    lambda: timmy > 5,
    lambda: wally.drive(speed=.5, turn=.5),
    lambda: izzy.motor_1.set(speed=.5),
    lambda: izzy.motor_1.set(speed=0)
]
# t1 = [
#     dict(cmd=wally.drive, speed=.5, turn=.5),
#     dict(cmd=izzy.motor_1.set, speed=.5),
#     {"cmd": izzy.motor_1.set, "speed": 0},
#     {"lambda": lambda: conner.__len__() > 5},
#     dict(cmd=wally.drive, speed=.5, turn=.5),
#     dict(cmd=izzy.motor_1.set, speed=.5),
#     {"cmd": izzy.motor_1.set, "speed": 0}
# ]
#


def run(books: list[dict[any]]):
    print(books)


def callit(cmd, **kwargs):
    print(cmd, kwargs)
    cmd(**kwargs)


def robot_init():
    m.find_outputs()


def teleop_periodic():
    m.check()
    m.rez()
    m.outputs_set()


if __name__ == '__main__':
    robot_init()
    # teleop_periodic()

    # pprint(m.outputs)
    print('******************')
    # pprint(m.agents)
    # m.check()

    # m.talk()
    # m.check()
    # m.rez()
    # pprint(m.agents_dict)
    # for name, agent in m.agents.items():
    #     print(f"{name = }")
    #     print(f"{agent = }")
    #     print(f'{agent["self"]}')

    print('******************')
    # m.outputs_set()

    # print(buttons)
    #
    # cool = {}
    # for count, button in enumerate(buttons, 1):
    #     cool[button] = count
    #
    # print(cool)
    #
    # the_coolest = {button: count for count, button in enumerate(buttons, 1)}
    #
    # axiss = ["l_stick_x", "l_stick_y", "l_trig", "r_trig", "r_stick_x", "r_stick_y"]
    # most_cool = {axis: count for count, axis in enumerate(axiss, 0)}
    #
    # print(the_coolest)
    #
    # print('***********************')
    # run(test_auto)
    #
    # phonecall = input("is the question")
    # print(phonecall)
    # if phonecall == "1":
    #     dance()
    #
    # next = input("is the question")
    # print(next)
    # print(phonecall + next)\
    #
    # def loop():
    #     while True:
    #         check_button()
    #
    #
    # while True:
    #     # in here we just ask human
    #     text = input('give me input')
    #     if text == 'dance':
    #         dance()
    #     elif text == 'loop':
    #         loop()
    name = {'name': 'archie'}

    archie = Autonomous()
    archie.run(ta)
    pprint(m.agents)

