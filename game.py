from board import Board
import pygame


class Game:

    def __init__(self,
                 height=480,
                 width=640,
                 cell_size=10,
                 cell_states='custom',
                 fps=10
                 ):

        self.width = width
        self.height = height
        self.cell_size = cell_size

        self.res = width, height
        self.surface = pygame.display.set_mode(self.res)

        self.cell_height = self.height // self.cell_size
        self.cell_width = self.width // self.cell_size

        self.cell_states = cell_states
        self.board = Board(self.cell_height, self.cell_width, self.cell_states)

        self.fps = fps
        self.generations = 0

    def DrawGrid(self):
        for x in range(0, self.width, self.cell_size):
            pygame.draw.line(
                self.surface,
                pygame.Color('dimgray'),
                (x, 0),
                (x, self.height)
            )
        for y in range(0, self.height, self.cell_size):
            pygame.draw.line(
                self.surface,
                pygame.Color('dimgray'),
                (0, y),
                (self.width, y)
            )

    def DrawCells(self):
        bias = self.cell_size
        for i in range(self.cell_height):
            for j in range(self.cell_width):
                if self.board.GetCellState(i, j) == 1:
                    color = 'yellow'
                else:
                    color = 'black'
                pygame.draw.rect(
                    self.surface,
                    pygame.Color(color),
                    (j * bias + 1, i * bias + 1, bias - 1, bias - 1)
                )

    def Next(self):
        next_board = Board(self.cell_height, self.cell_width)
        for i in range(self.cell_height):
            for j in range(self.cell_width):
                counter = self.board.NeighborCounter(i, j)
                if self.board.GetCellState(i, j) == 1:
                    counter -= 1
                    if counter == 2 or counter == 3:
                        next_board.ChangeCellState(i, j, 1)
                    else:
                        next_board.ChangeCellState(i, j, 0)
                else:
                    if counter == 3:
                        next_board.ChangeCellState(i, j, 1)
                    else:
                        next_board.ChangeCellState(i, j, 0)
        self.board = next_board
        self.generations += 1

    def GameIsOver(self):
        creatures = self.board.PositiveCellCounter()
        if creatures == 0:
            return True
        else:
            return False

    def Run(self):
        pygame.init()
        clock = pygame.time.Clock()
        pygame.display.set_caption('Life')
        self.surface.fill(pygame.Color('black'))
        condition = True
        if self.cell_states == 'custom':
            paused = True
        else:
            paused = False
        while condition:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    condition = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if pygame.mouse.get_pressed(3)[0]:
                        pos = pygame.mouse.get_pos()
                        x, y = [
                            pos[1] // self.cell_size,
                            pos[0] // self.cell_size,
                        ]
                        if self.board.GetCellState(x, y) == 1:
                            self.board.ChangeCellState(x, y, 0)
                        else:
                            self.board.ChangeCellState(x, y, 1)
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        paused = not paused
            self.DrawGrid()
            self.DrawCells()
            pygame.display.update()
            if paused:
                continue
            clock.tick(self.fps)
            if self.GameIsOver():
                condition = False
            self.Next()
        pygame.quit()
