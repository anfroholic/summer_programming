

class Mentor:
    def __init__(self, bubbles):
        self.name = bubbles

    def talk(self):
        print(f'hi my name is {self.name}')

    def praise(self):
        print('you made that, that looks real nice')


class BadMentor(Mentor):
    def __init__(self, bubbles):
        super().__init__(bubbles)

    def yells(self):
        print('We love you Yehansa!!!')

    def praise(self):
        super().praise()
        print('now throw it in the trash')


    andrew = BadMentor('andrew')
    matt = Mentor('matt')


    print(andrew.name)
    print(matt.name)

    andrew.talk()
    matt.talk()

    andrew.praise()
    matt.praise()


    andrew.yells()


