# Imports
import sys
import piece as PIECE
sys.path.append('../BoardStuff')


# Rook Object
class Rook(PIECE.Piece):

    def __init__(self, color):
        """
        Define Rook Class Variables
        """
        name = 'Rook'
        symbol_char = 'r'
        value = 5
        super().declare_variables(color, name, symbol_char, value)



    def get_potential_moves(self, row, col, board_height=8, board_width=8):

        routes = []

        # Up
        routes.append([[row - (i+1), col] for i in range(row)])

        # Down
        routes.append([[row + (i+1), col] for i in range(board_height-(row+1))])

        # Left
        routes.append([[row, col - (i+1)] for i in range(col)])

        # Right
        routes.append([[row, col + (i+1)] for i in range(board_width-(col+1))])

        for route in reversed(routes):
            if len(route) == 0:
                index = routes.index(route)
                routes.pop(index)

        origin = [row, col]
        return MOVE.Move.generate_moves(origin, routes)



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



# Rook Test
if __name__ == '__main__':
    p = Rook('black')
    print(p.color, p.name, p.value)

    print('\n---------------------------------------------------')
    print('For:', 0, 0)
    for move in p.get_potential_moves(0, 0):
        move.print_move()

    print('\n---------------------------------------------------')
    print('For:', 1, 1)
    for move in p.get_potential_moves(1, 1):
        move.print_move()

    print('\n---------------------------------------------------')
    print('For:', 4, 4)
    for move in p.get_potential_moves(4, 4):
        move.print_move()

    print('\n---------------------------------------------------')
    print('For:', 8, 8)
    for move in p.get_potential_moves(7, 7):
        move.print_move()

