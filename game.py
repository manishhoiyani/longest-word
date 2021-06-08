# game.py
# pylint: disable=missing-docstring

import string
import random

class Game:
    def __init__(self):
        self.grid = []
        for _ in range(9):
            self.grid.append(random.choice(string.ascii_uppercase))
import requests

class Game:
   def is_valid(self, word):
        return self.__check_dictionary(word)


@staticmethod
  def __check_dictionary(word):
        response = requests.get(f"https://wagon-dictionary.herokuapp.com/{word}")
        json_response = response.json()
        return json_response['found']