# game.py
# pylint: disable=missing-docstring
#pylint: disable=too-few-public-methods

import string
import random

class Game:
    def __init__(self):
        self.grid = []
        for _ in range(9):
            self.grid.append(random.choice(string.ascii_uppercase))