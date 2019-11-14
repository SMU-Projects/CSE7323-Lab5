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
        self._row = 0
        self._col = 0
        self._turn_last_moved = 0



    def _declare_variables(self, color, name, symbol_char, value):
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
        self._turn_last_moved = 0



    def _copy(self):
        """
        Creates a copy of piece
        :return: A copy of piece
        """
        p = Piece()
        p.color = self.color
        p.name = self.name
        p.symbol = self.symbol
        p.value = self.value
        p._turn_last_moved = self._turn_last_moved
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



    def _remove_blocked_attacking_coordinates(self, board, route):
        """
        From a move route, get the coordinates that are unblocked
        :param board:
        :param route:
        :return:
        """
        new_route = []
        for coordinate in route:
            r = coordinate[0]
            c = coordinate[1]
            new_route.append(coordinate)
            if board.grid[r][c].has_piece():
                return new_route
        return new_route



    def update_turn_last_moved(self, turn_count):
        """
        Updates turn_last_moved for the piece
        :param turn_count: The last turn this piece was moved on
        """
        self._turn_last_moved = turn_count



if __name__ == '__main__':
    p = Piece()
    print(p.color, p.name, p.symbol, p.value)
    p._declare_variables('white', 'Pawn', 'p', 1)
    print(p.color, p.name, p.symbol, p.value)
    p._declare_variables('red', 'Red Pawn', 'rp', 99)
    print('This should not print.')
