from game import Game

print('$ Hello, welcome to the Game Of Life!')
print('$ Would you like to start with a random field pattern or make it by yourself?')
print('[random | custom] >> ', end='')
field_type = input()
game = Game(cell_states=field_type)
game.Run()
