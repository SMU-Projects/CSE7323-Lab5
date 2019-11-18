# Imports
import sys
import copy as COPY
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
        self._turn_last_moved = -1



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
        self.value = value
        self._turn_last_moved = 0
        try:
            if color == 'white':
                self.symbol = 'w'+symbol_char
            elif color == 'black':
                self.symbol = 'b'+symbol_char
            else:
                raise ERROR.UndefinedPieceColor(self)
        except ERROR.UndefinedPieceColor as e:
            sys.exit(0)



    def _copy(self):
        """
        Creates a copy of piece using python's copy import
        :return: A copy of piece
        """
        p = COPY.copy(self)
        return p



    def get_available_coordinates(self, board):
        """
        Gets the available coordinates/squares for this piece
        :param board: The current state of the board
        :return: A list of available coordinates/squares
        """
        return []



    def get_attacking_coordinates(self, board):
        """
        Gets the attacking coordinates/squares for this piece
        :param board: The current state of the board
        :return: A list of attacking coordinates/squares
        """
        return []



    @staticmethod
    def _remove_blocked_attacking_coordinates(board, route):
        """
        From a move route, get the coordinates that are unblocked
        :param board: The current state of the board
        :param route: The route the piece is taking
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



    @staticmethod
    def _remove_out_of_range_coordinates(board, coordinates):
        """
        From a list of coordinates, remove coordinates that are out of range
        :param board: The current state of the board
        :param coordinates: A list of attacking or available coordinates
        :return: A list of attacking or available coordinates that are specifically in range of the board
        """
        for coordinate in reversed(coordinates):
            r = coordinate[0]
            c = coordinate[1]
            if r >= board.height or r < 0 or c >= board.width or c < 0:
                index = coordinates.index(coordinate)
                coordinates.pop(index)
        return coordinates



    @staticmethod
    def _remove_coordinates_with_given_color(color, board, coordinates):
        """
        From a list of coordinates, remove coordinates that that have the specified color
        :param color: color of team
        :param board: The current state of the board
        :param coordinates: A list of attacking or available coordinates
        :return: A list of attacking or available coordinates that don't have collisions with color
        """
        for coordinate in reversed(coordinates):
            r = coordinate[0]
            c = coordinate[1]
            if board.grid[r][c].piece.color == color:
                index = coordinates.index(coordinate)
                coordinates.pop(index)
        return coordinates



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
