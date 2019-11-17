# Imports
import sys
import player as PLAYER

class Human(PLAYER.Player):

    def __init__(self, color):
        """
        Initialization for Human Object; This Player class will serve as a Human Player
        """
        super().__init__(color)

    def request_move(self, board):
        """
        Asks the player what move to make, Player submits possible move to Chess game
        :return: a starting location and ending location for chess move
        """
        valid = False
        while not valid:
            try:
                start = input('Enter Start Position: ')
                end = input('Enter End Position: ')
                print()
                cf1 = start[0].upper()
                cr1 = int(start[1])
                cf2 = end[0].upper()
                cr2 = int(end[1])

                # Todo: Verify Input

                return cf1, cr1, cf2, cr2
            except:
                # Invalid Entry
                pass

