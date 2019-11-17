# Imports
import sys
import random
import player as PLAYER

class AI_Random(PLAYER.Player):

    def __init__(self, color):
        """
        Initialization for Random AI Object
        """
        super().__init__(color)

    def request_move(self, board):
        """
        Asks the AI what move to make, AI submits possible move to Chess game
        :return: a starting location and ending location for chess move
        """
        cf1 = self._alphabet[random.randint(0, 7)]
        cr1 = random.randint(1, 8)
        cf2 = self._alphabet[random.randint(0, 7)]
        cr2 = random.randint(1, 8)

        return cf1, cr1, cf2, cr2
