# Imports
import sys
sys.path.append('../BoardStuff')
import errors as ERROR

class Piece():

    def __init__(self):
        """
        Define Default Class Variables
        """
        self.color = 'null'
        self.name = 'null piece'
        self.symbol = '  '
        self.value = 0
        self.requires_board_state = False
        self.turn_last_moved = 0



    def declare_variables(self, color, name, symbol_char, value):
        """
        Define Class Variables
        :param color: Color of piece
        :param name: Name of piece
        :param symbol_char: Symbol Character for Piece
        :param value: Value of piece
        """
        self.color = color
        self.name = name
        try:
            if color == 'black':
                self.symbol = 'b'+symbol_char
            elif color == 'white':
                self.symbol = 'w'+symbol_char
            else:
                raise ERROR.UndefinedPieceColor(color, name)
        except ERROR.UndefinedPieceColor as e:
            sys.exit(0)
        self.value = value
        self.turn_last_moved = 0



    def copy(self):
        """
        Creates a copy of piece
        :return: A copy of piece
        """
        p = Piece()
        p.color = self.color
        p.name = self.name
        p.symbol = self.symbol
        p.value = self.value
        p.turn_last_moved = self.turn_last_moved
        return p



    def get_available_squares(self, board):
        """
        Gets the available squares for this piece
        :param board: The current state of the board
        :return: A list of available squares
        """
        pass



    def get_attacking_squares(self, board):
        """
        Gets the attacking squares for this piece
        :param board: The current state of the board
        :return: A list of attacking squares
        """
        pass



    def update_turn_last_moved(self, turn_count):
        """
        Updates turn_last_moved for the piece
        :param turn_count: The last turn this piece was moved on
        """
        self.turn_last_moved = turn_count




if __name__ == '__main__':
    p = Piece()
    print(p.color, p.name, p.symbol, p.value)
    p.declare_variables('white', 'Pawn', 'p', 1)
    print(p.color, p.name, p.symbol, p.value)
    p.declare_variables('red', 'Red Pawn', 'rp', 99)
    print('This should not print.')
