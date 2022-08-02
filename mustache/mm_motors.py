class MM_Motor:
    def __init__(self, name, can_id=99):
        self.name = name
        self.speed = 0
        self.can_id = can_id
        self.pos = 5
        self.zero_pos = 4

    def set(self, speed):
        self.speed = speed
        print(f'super speed is {self.speed + 5}, is that fast?')

    def _set(self):
        print(f'actually setting motor to {self.speed}')

    def __repr__(self):
        return f'the real {self.name} motor, and can_ID # {self.can_id}'

    def get_pos(self) -> float:
        return self.pos

    def reset_encoder(self):
        self.sero_pos = self.get_pos

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




