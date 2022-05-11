
class Agent:
    def __init__(self, superspy):
        self.name = superspy

    def __str__(self):
        return f"nice to meet you comrade I am {self.name}, I am a {self.__class__.__name__}"

    def check(self):
        pass

    def rez(self):
        pass