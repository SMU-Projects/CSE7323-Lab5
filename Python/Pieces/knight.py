# Imports
import sys
import piece as PIECE
sys.path.append('../BoardStuff')
import board as BOARD
import square as SQUARE


# Knight Object
class Knight(PIECE.Piece):

    def __init__(self, color):
        """
        Define Knight Class Variables
        """
        name = 'Knight'
        symbol_char = 'n'
        value = 3
        super().declare_variables(color, name, symbol_char, value)



    def get_available_coordinates(self, board):
        """
        Gets the available coordinates/squares for this piece
        :param board: The current state of the board
        :return: A list of available coordinates/squares
        """
        available_coordinates = self.get_attacking_coordinates(board)
        for coordinate in reversed(available_coordinates):
            r = coordinate[0]
            c = coordinate[1]
            if board.grid[r][c].has_piece():
                index = available_coordinates.index(coordinate)
                available_coordinates.pop(index)

        return available_coordinates



    def get_attacking_coordinates(self, board):
        """
        Gets the attacking coordinates/squares for this piece
        :param board: The current state of the board
        :return: A list of attacking coordinates/squares
        """
        attacking_coordinates = []
        attacking_coordinates.append([self.row-1, self.col-2])  # 1
        attacking_coordinates.append([self.row-2, self.col-1])  # 2
        attacking_coordinates.append([self.row-2, self.col+1])  # 3
        attacking_coordinates.append([self.row-1, self.col+2])  # 4
        attacking_coordinates.append([self.row+1, self.col+2])  # 5
        attacking_coordinates.append([self.row+2, self.col+1])  # 6
        attacking_coordinates.append([self.row+2, self.col-1])  # 7
        attacking_coordinates.append([self.row+1, self.col-2])  # 8

        for coordinate in reversed(attacking_coordinates):
            r = coordinate[0]
            c = coordinate[1]
            if r >= board.height or r < 0 or c >= board.width or c < 0:
                index = attacking_coordinates.index(coordinate)
                attacking_coordinates.pop(index)

        return attacking_coordinates



# Knight Test
if __name__ == '__main__':
    p = Knight('black')
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

