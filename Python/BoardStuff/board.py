import sys
import square as SQUARE

sys.path.append('../Pieces')
import piece as PIECE
# import pawn as PAWN
import rook as ROOK
# import knight as KNIGHT
# import bishop as BISHOP
# import queen as QUEEN
# import king as KING

class Board:

    def __init__(self):
        """
        Initialization of Board Object; Declaring Variables
        """
        self.alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        self.height = 8
        self.width = 8
        self.grid = [[SQUARE.Square() for c in range(self.width)] for r in range(self.height)]
        self.history = []

        self.move_count = 1 # Todo: move variable into Chess Class



    def _convert_coordinates(self, chess_file, chess_rank):
        """
        Converts Chess rank and file values to Array row and column values
        :param chess_file: File coordinate
        :param chess_rank: Rank coordinate
        :return: row, col from the file, rank
        """
        row = self.height - chess_rank
        col = self.alphabet.find(chess_file)
        return row, col



    def copy_board(self):
        """
        Creates and returns a copy of the board; called after every move to record board history
        """
        b = [[SQUARE.Square() for c in range(self.height)] for r in range(self.width)]
        for r in range(self.width):
            for c in range(self.height):
                b[r][c] = self.grid[r][c].copy()
        return b



    def set_piece(self, piece, chess_file, chess_rank):
        """
        Sets a piece on the Board
        :param piece: Piece to be set
        :param chess_file: File coordinate
        :param chess_rank: Rank coordinate
        """
        row, col = self._convert_coordinates(chess_file, chess_rank)
        square = self.grid[row][col]
        square.piece = piece



    def set_standard_board(self):
        """
        Sets the Board with the standard Chess Opening
        """
    #     white = 'white'
    #     black = 'black'
    #
    #     # Pawn
    #     for i in range(8):
    #         self.set_piece(PAWN.Pawn(white), self.alphabet[i], 2)
    #     for i in range(8):
    #         self.set_piece(PAWN.Pawn(black), self.alphabet[i], 7)

        # Rooks
        self.set_piece(ROOK.Rook(white), 'A', 1)
        self.set_piece(ROOK.Rook(white), 'H', 1)
        self.set_piece(ROOK.Rook(black), 'A', 8)
        self.set_piece(ROOK.Rook(black), 'H', 8)

    #     # Knights
    #     self.set_piece(KNIGHT.Knight(white), 'B', 1)
    #     self.set_piece(KNIGHT.Knight(white), 'G', 1)
    #     self.set_piece(KNIGHT.Knight(black), 'B', 8)
    #     self.set_piece(KNIGHT.Knight(black), 'G', 8)
    #
    #     # Bishops
    #     self.set_piece(BISHOP.Bishop(white), 'C', 1)
    #     self.set_piece(BISHOP.Bishop(white), 'F', 1)
    #     self.set_piece(BISHOP.Bishop(black), 'C', 8)
    #     self.set_piece(BISHOP.Bishop(black), 'F', 8)
    #
    #     # Queens
    #     self.set_piece(QUEEN.Queen(white), 'D', 1)
    #     self.set_piece(QUEEN.Queen(black), 'D', 8)
    #
    #     # Kings
    #     self.set_piece(KING.King(white), 'E', 1)
    #     self.set_piece(KING.King(black), 'E', 8)



    def print_board(self):
        """
        Prints a String visualization of the Board
        """
        file_header = '      '
        for i in range(8):
            file_header += self.alphabet[i] + '    '
        print(file_header)
        print('    -----------------------------------------')
        for r in range(len(self.grid)):
            line = ' ' + str(len(self.grid) - r) + '  |'
            for c in range(len(self.grid[r])):
                square = self.grid[r][c]
                symbol = square.piece.symbol
                line += ' ' + symbol + ' |'
            if r != int((self.height-1)/2) or self.move_count is None:
                print(line)
            else:
                print(line, end='')
                print('      Move: ' + str(self.move_count))
            print('    -----------------------------------------')
        print('\n')


if __name__ == '__main__':
    white = 'white'
    black = 'black'

    b = Board()
    b.print_board()
    # b.set_standard_board()
    # b.print_board()
    # print("Viable White Pawn Move:", b.move_piece(white, 'A', 2, 'A', 4))
    # print("Viable Black Pawn Move:", b.move_piece(black, 'B', 7, 'B', 5))
    # b.print_board()
