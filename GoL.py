import numpy as np
import matplotlib as plt
board_size = 50
class Game:
    def __init__(self):
        self.Board = np.zeros([board_size, board_size])



my_game = Game()
print(my_game.Board)