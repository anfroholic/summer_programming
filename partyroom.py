from rooms.conners_munch import Conveyor
from rooms.izzys_scoop import Intake
from config import con_conner, fake_conner
from agent import m

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


# an agency is born
fake_conner = Conveyor(**fake_conner)
conner = Conveyor(**con_conner)
izzy = Intake('izzy', conner)


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

    print('*****************')
    m.outputs_set()







