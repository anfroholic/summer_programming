from conners_munch import Conveyor
from izzys_scoop import Intake
from main import con_conner
from pprint import pprint

# an agency is born
conner = Conveyor(**con_conner)
izzy = Intake('izzy')


if __name__ == '__main__':
    agents = [conner, izzy]

    for agent in agents:
        print(agent.name)


    for agent in agents:
        print(agent)
        agent.check()
        agent.rez()




