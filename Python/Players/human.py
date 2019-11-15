# Imports
import sys
import player as PLAYER
sys.path.append('../BoardStuff')

class Human(PLAYER.Player):

    def __init__(self, color):
        """Initialization for Human Object; This Player class will serve as a Human Player"""
        super().__init__(color)

    def request_move(self):
        """Asks the player what move to make, Player submits possible move to Chess game"""
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

                human_move = MOVE.Move(starting=[cf1, cr1], attacking=[cf2, cr2])

                return human_move
            except:
                # Invalid Entry
                pass

