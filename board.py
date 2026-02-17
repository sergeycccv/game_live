from cell import Cell


class Board:
    def __init__(self, height, width, cell_states='random'):
        self.width = width
        self.height = height
        self.board = self.MakeNewBoard(cell_states)

    def MakeNewBoard(self, cell_states) -> list:
        board = [
            [Cell(cell_states) for _ in range(self.width)] for _ in range(self.height)
        ]
        return board

    def GetCellState(self, i, j) -> int:
        return self.board[i][j].GetState()

    def ChangeCellState(self, i, j, state):
        self.board[i][j].ChangeState(state)

    def OutBorder(self, i, j):
        return (
                i < 0 or
                j < 0 or
                i >= self.height or
                j >= self.width
        )

    def NeighborCounter(self, i, j):
        counter = 0
        for offset_i in range(-1, 2):
            for offset_j in range(-1, 2):
                if not self.OutBorder(i + offset_i, j + offset_j):
                    if self.GetCellState(i + offset_i, j + offset_j) == 1:
                        counter += 1
        return counter

    def PositiveCellCounter(self):
        counter = 0
        for i in range(self.height):
            for j in range(self.width):
                if self.board[i][j].GetState() == 1:
                    counter += 1
        return counter
