class Motor:
    def __init__(self, name):
        self.name = name
        self.speed = 0

    def set(self, speed):
        self.speed = speed
        print(f'super speed is {self.speed + 5}, is that fast?')
