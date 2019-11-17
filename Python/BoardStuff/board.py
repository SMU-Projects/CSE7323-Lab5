import sys
import square as SQUARE
import errors as ERROR

sys.path.append('../Pieces')
import piece as PIECE
import pawn as PAWN
import rook as ROOK
import knight as KNIGHT
import bishop as BISHOP
import queen as QUEEN
import king as KING

class Board:

    def __init__(self):
        """
        Initialization of Board Object; Declaring Variables
        """
        self.alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        self.height = 8
        self.width = 8
        self.grid = [[SQUARE.Square(r, c) for c in range(self.width)] for r in range(self.height)]
        self.history = []

        # Todo: move variables into Chess Class
        self.turn_count = 1
        self.turn_last_capture = 0
        self._has_king = False
        self.white_king_position = None
        self.black_king_position = None



    def _convert_to_array_coordinates(self, chess_file, chess_rank):
        """
        Converts Chess rank and file values to Array row and column values
        :param chess_file: File coordinate
        :param chess_rank: Rank coordinate
        :return: row, col for the file, rank
        """
        row = self.height - chess_rank
        col = self.alphabet.find(chess_file)
        return row, col



    def _convert_to_chess_coordinates(self, row, col):
        """
        Converts Array row and column values to Chess rank and file values
        :param row: Row coordinate
        :param col: Col coordinate
        :return: file, rank for the row, col
        """
        chess_file = self.alphabet[col]
        chess_rank = self.height - row

        return chess_file, chess_rank



    def copy_board_object(self):
        """
        Copies the Board object; this is particularly meant for AI's
        :return: the Board object
        """
        board = Board()
        board.height = self.height
        board.width = self.width
        board.grid = self._copy_grid()
        # board.history = self.history # This is kind of an expensive operation, imma leave it out for now
        board.turn_count = self.turn_count
        board.turn_last_capture = self.turn_last_capture
        board._has_king = self._has_king
        board.white_king_position = self.white_king_position
        board.black_king_position = self.black_king_position
        return board



    def _copy_grid(self):
        """
        Creates and returns a copy of Board.grid; called after every move to record board history
        """
        grid = [[SQUARE.Square(r, c) for c in range(self.height)] for r in range(self.width)]
        for r in range(self.width):
            for c in range(self.height):
                grid[r][c] = self.grid[r][c].copy()
        return grid



    def set_piece(self, piece, chess_file, chess_rank, debug=False):
        """
        Sets a piece on the Board
        :param piece: Piece to be set
        :param chess_file: File coordinate
        :param chess_rank: Rank coordinate
        :param debug: if debug, chess_file = row; chess_rank = col
        """
        if debug:
            row = chess_file
            col = chess_rank
        else:
            row, col = self._convert_to_array_coordinates(chess_file, chess_rank)
        if piece.name == "King":
            self._has_king = True
            try:
                if piece.color == 'white':
                    self.white_king_position = [row, col]
                elif piece.color == 'black':
                    self.black_king_position = [row, col]
                else:
                    raise ERROR.UndefinedPieceColor(piece)
            except ERROR.UndefinedPieceColor as e:
                sys.exit(0)
        elif piece.name == "Pawn":
            self.turn_last_capture = -1
        square = self.grid[row][col]
        if square.has_piece():
            self.turn_last_capture = -1
        square.set_piece(piece)



    def move_piece(self, color, cf1, cr1, cf2, cr2):
        """
        Moves a Piece from the starting Chess Position to an end Chess Position
        :param color: Color of Team
        :param cf1: First Chess File of Move
        :param cr1: First Chess Rank of Move
        :param cf2: Second Chess File of Move
        :param cr2: Second Chess Rank of Move
        :return: bool Whether or not the move was valid
        """
        row1, col1 = self._convert_to_array_coordinates(cf1, cr1)
        row2, col2 = self._convert_to_array_coordinates(cf2, cr2)
        valid, coordinate = self._is_valid_move(color, row1, col1, row2, col2)  # Does not evaluate Check

        if valid:
            self.execute_valid_move(start_coordinate=[row1, col1], end_coordinate=coordinate)

        return valid



    def execute_valid_move(self, start_coordinate, end_coordinate):
        """
        should not be called unless move is 100% verified to be valid
        :param start_coordinate:
        :param end_coordinate:
        :return:
        """
        row1 = start_coordinate[0]
        col1 = start_coordinate[1]
        row2 = end_coordinate[0]
        col2 = end_coordinate[1]
        color = self.grid[row1][col1].piece.color

        previous_grid = self._copy_grid()

        # Grab Squares
        start_square = self.grid[row1][col1]
        end_square = self.grid[row2][col2]

        if end_coordinate[-1] == 'is_queening':
            self.set_piece(QUEEN.Queen(color), row2, col2, debug=True)
        else:
            self.set_piece(start_square.piece, row2, col2, debug=True)
        end_square.piece.update_turn_last_moved(self.turn_count)
        if end_coordinate[-1] == 'is_en_passant':
            self.set_piece(PIECE.Piece(), row1, col2, debug=True)
        start_square.set_piece(PIECE.Piece())

        if end_coordinate[-1] == 'is_castling':
            if col2 - col1 > 0: # King Side Castle
                self.set_piece(self.grid[row2][col2 + 1].piece, row2, col2 - 1, debug=True)
                self.grid[row2][col2 - 1].piece.update_turn_last_moved(self.turn_count)
                self.set_piece(PIECE.Piece(), row2, col2 + 1, debug=True)
            else: # Queen Side Castle
                self.set_piece(self.grid[row2][col2 - 2].piece, row2, col2 + 1, debug=True)
                self.grid[row2][col2 + 1].piece.update_turn_last_moved(self.turn_count)
                self.set_piece(PIECE.Piece(), row2, col2 - 2, debug=True)

        # Add the previous position to history
        self.history.append(previous_grid)

        # Update Turn Variables
        self.turn_count += 1
        self.turn_last_capture += 1



    def _is_valid_move(self, color, row1, col1, row2, col2):
        """
        Checks to see if move is valid and flags if the move is an En Passant, a Castling, or Queening move
        :param color: Color of Team
        :param row1: First Row Number of Move
        :param col1: First Col Number of Move
        :param row2: Second Row Number of Move
        :param col2: Second Col Number of Move
        :return: Returns dictionary with keys: valid, is_castling, is_en_passant, is_queening; values are bool
        """

        # Check to see if rows or cols are outside bounds
        if row1 >= self.height or row1 < 0 or row2 >= self.height or row2 < 0:
            return False, []
        if col1 >= self.width or col1 < 0 or col2 >= self.width or col2 < 0:
            return False, []

        # Get starting square piece
        start_square_piece = self.grid[row1][col1].piece

        # Check to see if selected piece is correct color
        if start_square_piece.color != color:
            return False, []

        # Gets all available coordinates for piece
        valid_available_coordinates = self.get_valid_available_coordinates(start_square_piece)

        # Check to see if move is found in the available coordinates
        attack_coordinate = [row2, col2]
        for coordinate in valid_available_coordinates:
            if attack_coordinate == coordinate[0:2]:
                return True, coordinate

        return False, []



    def get_valid_available_coordinates(self, piece):
        """
        idk yet
        :param piece:
        :return:
        """

        row1 = piece.row
        col1 = piece.col
        color = piece.color

        piece = self.grid[row1][col1].piece
        available_coordinates = piece.get_available_coordinates(self)

        # If there is no king, all available coordinates are valid one
        if not self._has_king:
            return available_coordinates

        # Build a valid available coordinates list
        valid_available_coordinates = []

        # For every available move in coordinate...
        for coordinate in available_coordinates:

            # Copy grid and evaluate new position
            previous_grid = self._copy_grid()
            row2 = coordinate[0]
            col2 = coordinate[1]

            # Grab Squares
            start_square = self.grid[row1][col1]
            end_square = self.grid[coordinate[0]][col2]

            # Use Square's set_piece rather than self's because self's variables should not be updated
            end_square.set_piece(start_square.piece)
            if len(coordinate) != 2 and coordinate[-1] == 'is_en_passant':
                self.grid[row1][col2].set_piece(PIECE.Piece())
            start_square.set_piece(PIECE.Piece())

            # Are we in Check?
            if end_square.piece.name == 'King':
                check = self.is_coordinate_in_check(color, row2, col2)
            else:
                if color == "white":
                    check = self.is_coordinate_in_check(color, self.white_king_position[0], self.white_king_position[1])
                else:
                    check = self.is_coordinate_in_check(color, self.black_king_position[0], self.black_king_position[1])
            if not check:
                valid_available_coordinates.append(coordinate)

            self.grid = previous_grid

        return valid_available_coordinates



    def is_coordinate_in_check(self, color, row, col):
        """
        Checks to see if a given coordinate is in check
        :param color: Color of Team
        :param row: Row of coordinate
        :param col: Col of coordinate
        :return: bool Whether the coordinate is in check or not
        """
        in_check_coordinate = [row, col]
        for r in range(self.height):
            for c in range(self.width):
                piece = self.grid[r][c].piece
                if piece.color != color:
                    attack_coordinates = piece.get_attacking_coordinates(self)
                    for coordinate in attack_coordinates:
                        if coordinate == in_check_coordinate:
                            return True
        return False



    def is_checkmate(self, color):
        """
        Checks to see if the specified team is in checkmate
        :param color: Color of team that might be in checkmate
        :return: bool Whether the team is in checkmate or not
        """
        # Check if position is first in check; Assume only two teams
        if color == "white":
            if not self.is_coordinate_in_check(color, self.white_king_position[0], self.white_king_position[1]):
                return False
        else:
            if not self.is_coordinate_in_check(color, self.black_king_position[0], self.black_king_position[1]):
                return False

        # Does the team have any available moves to get out of check?
        for r in range(self.height):
            for c in range(self.width):
                piece = self.grid[r][c].piece
                if piece.color == color:
                    if len(self.get_valid_available_coordinates(piece)) > 0:
                        return False

        # No valid available coordinates were found, this is checkmate
        return True



    def is_draw(self, color):
        """
        Checks to see if the specified team is in a draw
        :param color: Color of team that might be in a draw
        :return: bool Whether the team is in a draw or not
        """

        # insufficient_material = False
        # TODO: Check for insufficient material

        # fifty_move_draw = False
        if self.turn_last_capture >= 100:
            return True

        # # threefold_repetition = False
        # if len(self.history) > 4:
        #     if self.grid == self.history[-2] == self.history[-4]:
        #         return True

        # stalemate = False
        for r in range(self.height):
            for c in range(self.width):
                piece = self.grid[r][c].piece
                if piece.color == color:
                    if len(self.get_valid_available_coordinates(piece)) > 0:
                        return False
        return True



    def set_standard_board(self):
        """
        Sets the Board with the standard Chess Opening
        """
        white = 'white'
        black = 'black'

        # Pawn
        for i in range(8):
            self.set_piece(PAWN.Pawn(white), self.alphabet[i], 2)
        for i in range(8):
            self.set_piece(PAWN.Pawn(black), self.alphabet[i], 7)

        # Rooks
        self.set_piece(ROOK.Rook(white), 'A', 1)
        self.set_piece(ROOK.Rook(white), 'H', 1)
        self.set_piece(ROOK.Rook(black), 'A', 8)
        self.set_piece(ROOK.Rook(black), 'H', 8)

        # Knights
        self.set_piece(KNIGHT.Knight(white), 'B', 1)
        self.set_piece(KNIGHT.Knight(white), 'G', 1)
        self.set_piece(KNIGHT.Knight(black), 'B', 8)
        self.set_piece(KNIGHT.Knight(black), 'G', 8)

        # Bishops
        self.set_piece(BISHOP.Bishop(white), 'C', 1)
        self.set_piece(BISHOP.Bishop(white), 'F', 1)
        self.set_piece(BISHOP.Bishop(black), 'C', 8)
        self.set_piece(BISHOP.Bishop(black), 'F', 8)

        # Queens
        self.set_piece(QUEEN.Queen(white), 'D', 1)
        self.set_piece(QUEEN.Queen(black), 'D', 8)

        # Kings
        self.set_piece(KING.King(white), 'E', 1)
        self.set_piece(KING.King(black), 'E', 8)



    def print_board(self, debug=False):
        """
        Prints a String visualization of the Board
        :param debug: if debug, print board in debug mode
        """
        file_header = '      '
        if debug:
            for i in range(8):
                file_header += str(i) + '    '
        else:
            for i in range(8):
                file_header += self.alphabet[i] + '    '
        print(file_header)
        print('    -----------------------------------------')
        for r in range(len(self.grid)):
            if debug:
                line = ' ' + str(r) + '  |'
            else:
                line = ' ' + str(len(self.grid) - r) + '  |'
            for c in range(len(self.grid[r])):
                square = self.grid[r][c]
                symbol = square.piece.symbol
                line += ' ' + symbol + ' |'
            if r != int((self.height-1)/2) or self.turn_count is None:
                print(line)
            else:
                print(line, end='')
                print('      Move: ' + str(self.turn_count))
            print('    -----------------------------------------')
        print('\n')



if __name__ == '__main__':
    white = 'white'
    black = 'black'

    b = Board()
    b.print_board()
    b.print_board(True)
    b.set_standard_board()
    b.print_board()
    print("Viable White Knight Move:", b.move_piece(white, 'G', 1, 'F', 3))
    print("Viable Black Knight Move:", b.move_piece(black, 'B', 8, 'C', 6))
    b.print_board()

    print("Viable Black Knight Move:", b.move_piece(black, 'C', 6, 'E', 5))
    b.print_board()

    print("Knight is in Check:", b.is_coordinate_in_check(black, 3, 4))
