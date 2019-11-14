# Imports
import sys
import piece as PIECE
sys.path.append('../BoardStuff')
import board as BOARD


# King Object
class King(PIECE.Piece):

    def __init__(self, color):
        """
        Define King Class Variables
        """
        super()
        self._declare_variables(color=color, name='King', symbol_char='k', value=10000)



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
            if board.grid[r][c].piece.color == self.color:
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
        attacking_coordinates.append([self.row-1, self.col-1])  # Move King Up Left
        attacking_coordinates.append([self.row-1, self.col+1])  # Move King Up Right
        attacking_coordinates.append([self.row+1, self.col+1])  # Move King Down Right
        attacking_coordinates.append([self.row+1, self.col-1])  # Move King Down Left

        attacking_coordinates.append([self.row-1, self.col])  # Move King Up
        attacking_coordinates.append([self.row+1, self.col])  # Move King Down
        attacking_coordinates.append([self.row, self.col-1])  # Move King Left
        attacking_coordinates.append([self.row, self.col+1])  # Move King Left

        # Castling ########## TODO: Check for Check in King Passing Squares
        if self.turn_last_moved == 0: # The following routes are the passing squares, and then ending square
            # White's King Side Castle
            if self.color == 'white' and board[7][7].piece.turn_last_moved == 0: # Hardcoded King Rook's Position
                routes.append([[row, col+1], [row, col+2], [row, col+2, 'isCastling']])
            # White's Queen Side Castle
            if self.color == 'white' and board[7][0].piece.turn_last_moved == 0: # Hardcoded Queen Rook's Position
                routes.append([[row, col-1], [row, col-2], [row, col-3], [row, col-2, 'isCastling']])
            # Black's King Side Castle
            if self.color == 'black' and board[0][7].piece.turn_last_moved == 0: # Hardcoded King Rook's Position
                routes.append([[row, col+1], [row, col+2], [row, col+2, 'isCastling']])
            # Black's Queen Side Castle
            if self.color == 'black' and board[0][0].piece.turn_last_moved == 0: # Hardcoded Queen Rook's Position
                routes.append([[row, col-1], [row, col-2], [row, col-3], [row, col-2, 'isCastling']])

        for coordinate in reversed(attacking_coordinates):
            r = coordinate[0]
            c = coordinate[1]
            if r >= board.height or r < 0 or c >= board.width or c < 0:
                index = attacking_coordinates.index(coordinate)
                attacking_coordinates.pop(index)

        return attacking_coordinates



# King Test
if __name__ == '__main__':
    p = King('black')
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


