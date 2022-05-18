import main
from rooms.conners_munch import Conveyor
from rooms.izzys_scoop import Intake
from main import con_conner

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
fake_conner = Conveyor(**main.fake_conner)
conner = Conveyor(**con_conner)
izzy = Intake('izzy', fake_conner)


if __name__ == '__main__':
    agents = [izzy,conner]

    for agent in agents:
        print(agent.name)


    for agent in agents:
        print(agent)
        agent.check()
        agent.rez()




