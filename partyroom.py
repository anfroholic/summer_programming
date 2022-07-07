from rooms.conners_munch import Conveyor
from rooms.izzys_scoop import Intake
from config import con_conner, fake_conner
from agent import m
from rooms.driver import Driver

from mm_motors import MM_Motor

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
fake_conner = Conveyor(driver=driver, **fake_conner)
conner = Conveyor(driver=driver, **con_conner)
izzy = Intake(name='izzy', conner=conner, driver=driver)



def robot_init():
    m.find_outputs()


def teleop_periodic():
    m.check()
    m.rez()
    m.outputs_set()



if __name__ == '__main__':
    robot_init()
    #teleop_periodic()

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

    print(buttons)

    cool = {}
    for count, button in enumerate(buttons, 1):
        cool[button] = count

    print(cool)

    the_coolest = {button: count for count, button in enumerate(buttons, 1)}

    axiss = ["l_stick_x", "l_stick_y", "l_trig", "r_trig", "r_stick_x", "r_stick_y"]
    most_cool ={axis: count for count, axis in enumerate(axiss, 0)}

    print(the_coolest)






