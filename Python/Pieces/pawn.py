# Imports
import sys
import piece as PIECE
sys.path.append('../BoardStuff')
import board as BOARD


# Pawn Object
class Pawn(PIECE.Piece):

    # Define Class Variables
    def __init__(self, color):
        """
        Define King Class Variables
        """
        # Get Pawn direction from color
        if color == 'white':
            self.pawn_direction = -1
        else:
            self.pawn_direction = 1

        super()
        self._declare_variables(color=color, name='Pawn', symbol_char='p', value=1)



    def get_available_coordinates(self, board):
        """
        Gets the available coordinates/squares for this piece
        :param board: The current state of the board
        :return: A list of available coordinates/squares
        """
        available_coordinates = []

        # Normal Non-attack
        # moving 1 square
        square1 = board.grid[self.row + self.pawn_direction][self.col]
        if square1.piece.color == 'null':
            available_coordinates.append([self.row + self.pawn_direction, self.col])
        # moving 2 squares
        if self._turn_last_moved == 0:
            square2 = board.grid[self.row + 2 * self.pawn_direction][self.col]
            if square1.piece.color == 'null' and square2.piece.color == 'null':
                available_coordinates.append([self.row + 2*self.pawn_direction, self.col])


        # Normal Attack
        if self.col-1 >= 0:
            square = board.grid[self.row + self.pawn_direction][self.col-1]
            if square.piece.color != 'null' and square.piece.color != self.color:
                available_coordinates.append([self.row + self.pawn_direction, self.col-1])
        if self.col+1 < board.width:
            square = board.grid[self.row + self.pawn_direction][self.col+1]
            if square.piece.color != 'null' and square.piece.color != self.color:
                available_coordinates.append([self.row + self.pawn_direction, self.col+1])

        # En Passant
        if self.color == 'white' and self.row == 3: # This is hardcoded to be the 5 rank
            if self.col-1 >= 0:
                square = board.grid[self.row][self.col-1]
                if square.piece.color == 'black' and square.piece.name == 'Pawn' \
                        and (square.piece._turn_last_moved == board.turn_count-1):
                    available_coordinates.append([self.row + self.pawn_direction, self.col-1, "is_en_passant"])
            if self.col+1 < board.width:
                square = board.grid[self.row][self.col+1]
                if square.piece.color == 'black' and square.piece.name == 'Pawn' \
                        and (square.piece._turn_last_moved == board.turn_count-1):
                    available_coordinates.append([self.row + self.pawn_direction, self.col+1, "is_en_passant"])

        if self.color == 'black' and self.row == 4: # This is hardcoded to be the 4 rank
            if self.col-1 >= 0:
                square = board.grid[self.row][self.col-1]
                if square.piece.color == 'white' and square.piece.name == 'Pawn' \
                        and (square.piece._turn_last_moved == board.turn_count-1):
                    available_coordinates.append([self.row + self.pawn_direction, self.col-1, "is_en_passant"])
            if self.col+1 < board.width:
                square = board.grid[self.row][self.col+1]
                if square.piece.color == 'white' and square.piece.name == 'Pawn' \
                        and (square.piece._turn_last_moved == board.turn_count-1):
                    available_coordinates.append([self.row + self.pawn_direction, self.col+1, "is_en_passant"])

        for coordinate in reversed(available_coordinates):
            r = coordinate[0]
            c = coordinate[1]
            if r >= board.height or r < 0 or c >= board.width or c < 0:
                index = available_coordinates.index(coordinate)
                available_coordinates.pop(index)
            if (self.color == "white" and r == 0) or (self.color == "black" and r == board.height-1):
                coordinate.append("is_queening")

        return available_coordinates



    def get_attacking_coordinates(self, board):
        """
        Gets the attacking coordinates/squares for this piece
        :param board: The current state of the board
        :return: A list of attacking coordinates/squares
        """
        attacking_coordinates = []

        # Normal Attack
        if self.col-1 >= 0:
            attacking_coordinates.append([self.row + self.pawn_direction, self.col-1])
        if self.col+1 < board.width:
            attacking_coordinates.append([self.row + self.pawn_direction, self.col+1])

        return attacking_coordinates



# Pawn Test
if __name__ == '__main__':
    p = Pawn('black')
    print(p.color, p.name, p.value)
    b = BOARD.Board()

    print('\n---------------------------------------------------')
    b.set_piece(p, 1, 1, debug=True)
    b.print_board(debug=True)
    print('For:', 1, 1)
    for available_coordinates in p.get_available_coordinates(b):
        print(available_coordinates)

    print('\n---------------------------------------------------')
    b.set_piece(p, 1, 6, debug=True)
    b.print_board(debug=True)
    print('For:', 1, 6)
    for available_coordinates in p.get_available_coordinates(b):
        print(available_coordinates)

    print('\n---------------------------------------------------')
    p._turn_last_moved = 10
    b.set_piece(p, 6, 4, debug=True)
    b.print_board(debug=True)
    print('For:', 6, 4)
    for available_coordinates in p.get_available_coordinates(b):
        print(available_coordinates)
