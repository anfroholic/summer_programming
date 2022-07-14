class MM_Motor:
    def __init__(self, name):
        self.name = name
        self.speed = 0

    def set(self, speed):
        self.speed = speed
        print(f'super speed is {self.speed + 5}, is that fast?')

    def _set(self):
        print(f'actually setting motor to {self.speed}')

    def __repr__(self):
        return f'the real {self.name} motor'

class MM_Output:
    def __init__(self, name: str, state: bool, pin: int):
        self.name = name
        self.state = state
        self.pin = pin

    def set(self, state: bool):
        self.state = state
        print(f"how are you feeling {state}")

    def _set(self):
        print(f"{self.state} is happening  >:0")

    def __repr__(self):
        return f"{self.name} real outputs"




