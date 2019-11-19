# Imports
import sys

sys.path.append('../Players')
import human as HUMAN
import ai_random as AI_RANDOM
import ai_cnn1 as AI_CNN1

sys.path.append('../BoardStuff')
import board as BOARD
import square as SQUARE

sys.path.append('../Pieces')
import piece as PIECE
import pawn as PAWN
import rook as ROOK
import knight as KNIGHT
import bishop as BISHOP
import queen as QUEEN
import king as KING

class Chess:

    def __init__(self):
        """
        Initialization for Chess Object
        """

        # Setup chess board
        self.chess_board = BOARD.Board()
        self.chess_board.set_standard_board()

        # Declare game over conditions
        self.is_checkmate = False
        self.is_draw = False

        # Declare players
        self.white_player = None
        self.black_player = None

        # Other
        self.white_turn = True

    def setup_game(self):
        """
        Setup players and rules for Chess Game
        """
        # Redeclare players
        # self.white_player = HUMAN.Human('white')
        # self.white_player = AI_RANDOM.AI_Random('white')
        self.white_player = AI_CNN1.AI_Cnn1('white', '../Models/cnn3.h5')
        # self.black_player = HUMAN.Human('black')
        self.black_player = AI_RANDOM.AI_Random('black')
        # self.black_player = AI_CNN1.AI_Cnn1('black', '../Models/cnn3.h5')

    def begin_game(self):
        """
        Game Loop for Chess Game
        :return: is_checkmate, is_draw
        """
        self.chess_board.print_board()
        while not self.is_checkmate and not self.is_draw:

            valid = False
            while not valid:
                # Request move from player
                if self.white_turn:
                    cf1, cr1, cf2, cr2 = self.white_player.request_move(self.chess_board)
                    valid = self.chess_board.move_piece(self.white_player.color, cf1, cr1, cf2, cr2)
                else:
                    cf1, cr1, cf2, cr2 = self.black_player.request_move(self.chess_board)
                    valid = self.chess_board.move_piece(self.black_player.color, cf1, cr1, cf2, cr2)

            # After valid move change player's turn and check for game over condition
            if self.white_turn:
                self.white_turn = False
                self.is_checkmate = self.chess_board.is_checkmate("black")
                if not self.is_checkmate:
                    self.is_draw = self.chess_board.is_draw("black")
            else:
                self.white_turn = True
                self.is_checkmate = self.chess_board.is_checkmate("white")
                if not self.is_checkmate:
                    self.is_draw = self.chess_board.is_draw("white")

            self.chess_board.print_board()

        if self.is_checkmate:
            if self.white_turn:
                print("Black Wins")
            else:
                print("White Wins")

        if self.is_draw:
            print("Draw")

        return self.is_checkmate, self.is_draw



# Run Game
if __name__ == '__main__':
    chess_game = Chess()
    chess_game.setup_game()
    chess_game.begin_game()
