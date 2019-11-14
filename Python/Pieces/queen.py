# Imports
import sys
import piece as PIECE
import bishop as BISHOP
sys.path.append('../BoardStuff')
import board as BOARD


# Queen Object
class Queen(PIECE.Piece):

    def __init__(self, color):
        """
        Define Queen Class Variables
        """
        super()
        self._declare_variables(color=color, name='Queen', symbol_char='q', value=9)



    def get_available_coordinates(self, board):
        """
        Gets the available coordinates/squares for this piece
        :param board: The current state of the board
        :return: A list of available coordinates/squares
        """
        available_coordinates = self.get_attacking_coordinates(board)
        available_coordinates = self._remove_coordinates_with_given_color(self.color, board, available_coordinates)
        return available_coordinates



    def get_attacking_coordinates(self, board):
        """
        Gets the attacking coordinates/squares for this piece
        :param board: The current state of the board
        :return: A list of attacking coordinates/squares
        """
        attacking_coordinates = []

        # Move Queen Up Left
        up_left = list()
        up_left.extend(BISHOP.Bishop._get_diagonal_route(self.row, self.col, up=True, left=True))
        up_left = self._remove_blocked_attacking_coordinates(board, up_left)
        attacking_coordinates.extend(up_left)

        # Move Queen Up Right
        up_right = list()
        up_right.extend(BISHOP.Bishop._get_diagonal_route(self.row, self.col, up=True, left=False))
        up_right = self._remove_blocked_attacking_coordinates(board, up_right)
        attacking_coordinates.extend(up_right)

        # Move Queen Down Right
        down_right = list()
        down_right.extend(BISHOP.Bishop._get_diagonal_route(self.row, self.col, up=False, left=False))
        down_right = self._remove_blocked_attacking_coordinates(board, down_right)
        attacking_coordinates.extend(down_right)

        # Move Queen Down Left
        down_left = list()
        down_left.extend(BISHOP.Bishop._get_diagonal_route(self.row, self.col, up=False, left=True))
        down_left = self._remove_blocked_attacking_coordinates(board, down_left)
        attacking_coordinates.extend(down_left)

        # Move Queen Up
        up = list()
        for i in range(self.row):
            up.append([self.row - (i+1), self.col])
        up = self._remove_blocked_attacking_coordinates(board, up)
        attacking_coordinates.extend(up)

        # Move Queen Down
        down = list()
        for i in range(board.height-(self.row+1)):
            down.append([self.row + (i+1), self.col])
        down = self._remove_blocked_attacking_coordinates(board, down)
        attacking_coordinates.extend(down)

        # Move Queen Left
        left = list()
        for i in range(self.col):
            left.append([self.row, self.col - (i+1)])
        left = self._remove_blocked_attacking_coordinates(board, left)
        attacking_coordinates.extend(left)

        # Move Queen Right
        right = list()
        for i in range(board.width-(self.col+1)):
            right.append([self.row, self.col + (i+1)])
        right = self._remove_blocked_attacking_coordinates(board, right)
        attacking_coordinates.extend(right)

        return attacking_coordinates



# Queen Test
if __name__ == '__main__':
    p = Queen('black')
    print(p.color, p.name, p.value)
    b = BOARD.Board()

    print('\n---------------------------------------------------')
    b.set_piece(p, 0, 0, debug=True)
    b.print_board(debug=True)
    print('For:', 0, 0)
    for available_coordinates in p.get_available_coordinates(b):
        print(available_coordinates)

    print('\n---------------------------------------------------')
    b.set_piece(p, 1, 1, debug=True)
    b.print_board(debug=True)
    print('For:', 1, 1)
    for available_coordinates in p.get_available_coordinates(b):
        print(available_coordinates)

    print('\n---------------------------------------------------')
    b.set_piece(p, 4, 4, debug=True)
    b.print_board(debug=True)
    print('For:', 4, 4)
    for available_coordinates in p.get_available_coordinates(b):
        print(available_coordinates)

    print('\n---------------------------------------------------')
    b.set_piece(p, 7, 7, debug=True)
    b.print_board(debug=True)
    print('For:', 7, 7)
    for available_coordinates in p.get_available_coordinates(b):
        print(available_coordinates)

