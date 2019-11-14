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
        self.row = 0
        self.col = 0
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



    def get_available_coordinates(self, board):
        """
        Gets the available coordinates/squares for this piece
        :param board: The current state of the board
        :return: A list of available coordinates/squares
        """
        pass



    def get_attacking_coordinates(self, board):
        """
        Gets the attacking coordinates/squares for this piece
        :param board: The current state of the board
        :return: A list of attacking coordinates/squares
        """
        pass



    def is_move_blocked(self, board, row1, col1, row2, col2):
        """
        Checks to see if move path has an obstruction or is blocked
        :param row1:
        :param col1:
        :param row2:
        :param col2:
        :return: bool Whether the move is blocked
        """
        pass
        # blocked = False
        # for coordinate in move.pass_coordinates:
        #     r = coordinate[0]
        #     c = coordinate[1]
        #     pass_square = self.grid[r][c]
        #     if pass_square.has_piece():
        #         blocked = True
        # return blocked



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
