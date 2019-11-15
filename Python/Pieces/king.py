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
        available_coordinates = self._remove_coordinates_with_given_color(self.color, board, available_coordinates)

        # Castling TODO: Check for Check in King Passing Squares
        if self._turn_last_moved == 0 and not board.is_coordinate_in_check(self.color, self.row, self.col):
            # White's King Side Castle
            if self.color == 'white' and board.grid[7][7].piece._turn_last_moved == 0:  # Hardcoded King Rook's Position
                if not board.grid[self.row][self.col+1].has_piece() and not board.is_coordinate_in_check(self.color, self.row, self.col+1) \
                        and not board.grid[self.row][self.col+2].has_piece() and not board.is_coordinate_in_check(self.color, self.row, self.col+2):
                    available_coordinates.append([self.row, self.col+2, 'is_castling'])
            # White's Queen Side Castle
            if self.color == 'white' and board.grid[7][0].piece._turn_last_moved == 0:  # Hardcoded Queen Rook's Position
                if not board.grid[self.row][self.col-1].has_piece() and not board.is_coordinate_in_check(self.color, self.row, self.col-1) \
                        and not board.grid[self.row][self.col-2].has_piece() and not board.is_coordinate_in_check(self.color, self.row, self.col-2) \
                        and not board.grid[self.row][self.col-3].has_piece():
                    available_coordinates.append([self.row, self.col-2, 'is_castling'])
            # Black's King Side Castle
            if self.color == 'black' and board.grid[0][7].piece._turn_last_moved == 0:  # Hardcoded King Rook's Position
                if not board.grid[self.row][self.col+1].has_piece() and not board.is_coordinate_in_check(self.color, self.row, self.col+1) \
                        and not board.grid[self.row][self.col+2].has_piece() and not board.is_coordinate_in_check(self.color, self.row, self.col+2):
                    available_coordinates.append([self.row, self.col+2, 'is_castling'])
            # Black's Queen Side Castle
            if self.color == 'black' and board.grid[0][0].piece._turn_last_moved == 0:  # Hardcoded Queen Rook's Position
                if not board.grid[self.row][self.col-1].has_piece() and not board.is_coordinate_in_check(self.color, self.row, self.col-1) \
                        and not board.grid[self.row][self.col-2].has_piece() and not board.is_coordinate_in_check(self.color, self.row, self.col-2) \
                        and not board.grid[self.row][self.col-3].has_piece():
                    available_coordinates.append([self.row, self.col-2, 'is_castling'])

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

        attacking_coordinates = self._remove_out_of_range_coordinates(board, attacking_coordinates)

        return attacking_coordinates



# King Test
if __name__ == '__main__':
    p = King('black')
    p.update_turn_last_moved(10)
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


