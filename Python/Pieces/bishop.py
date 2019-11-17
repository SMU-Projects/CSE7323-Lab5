# Imports
import sys
import piece as PIECE
sys.path.append('../BoardStuff')
import board as BOARD


# Bishop Object
class Bishop(PIECE.Piece):

    def __init__(self, color):
        """
        Define Bishop Class Variables
        """
        super()
        self._declare_variables(color=color, name='Bishop', symbol_char='b', value=3.5)



    @staticmethod
    def _get_diagonal_route(r, c, up, left, board_height=8, board_width=8):
        """
        Gets the specified diagonal route stemming from a given row or col
        :param r: row position
        :param c: col position
        :param up: bool Whether if up or down
        :param left: bool Whether if left or right
        :param board_height: height of board
        :param board_width: width of board
        :return: route of diagonal move
        """
        route = []
        if up:
            r_direction = -1
        else:
            r_direction = 1
        if left:
            c_direction = -1
        else:
            c_direction = 1
        r += r_direction
        c += c_direction
        while r >= 0 and c >= 0 and r < board_height and c < board_width:
            route.append([r, c])
            r += r_direction
            c += c_direction
        return route




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

        # Move Bishop Up Left
        up_left = list()
        up_left.extend(self._get_diagonal_route(self.row, self.col, up=True, left=True))
        up_left = self._remove_blocked_attacking_coordinates(board, up_left)
        attacking_coordinates.extend(up_left)

        # Move Bishop Up Right
        up_right = list()
        up_right.extend(self._get_diagonal_route(self.row, self.col, up=True, left=False))
        up_right = self._remove_blocked_attacking_coordinates(board, up_right)
        attacking_coordinates.extend(up_right)

        # Move Bishop Down Right
        down_right = list()
        down_right.extend(self._get_diagonal_route(self.row, self.col, up=False, left=False))
        down_right = self._remove_blocked_attacking_coordinates(board, down_right)
        attacking_coordinates.extend(down_right)

        # Move Bishop Down Left
        down_left = list()
        down_left.extend(self._get_diagonal_route(self.row, self.col, up=False, left=True))
        down_left = self._remove_blocked_attacking_coordinates(board, down_left)
        attacking_coordinates.extend(down_left)

        return attacking_coordinates



# Bishop Test
if __name__ == '__main__':
    p = Bishop('black')
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
