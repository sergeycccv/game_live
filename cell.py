import random


class Cell:
    def __init__(self, cell_states='random') -> None:
        if cell_states == 'random':
            self.state = random.randint(0, 1)
        else:
            self.state = 0

    def GetState(self) -> int:
        return self.state

    def ChangeState(self, state):
        self.state = state
