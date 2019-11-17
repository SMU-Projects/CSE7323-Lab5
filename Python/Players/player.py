# Imports

class Player:

    def __init__(self, color):
        """
        Initialization for Player Object; Base class for various Chess players
        """
        self.color = color
        self._alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    def request_move(self, board):
        """
        Unwritten base function for Player Class, will ask the player what move to make
        """
        pass
