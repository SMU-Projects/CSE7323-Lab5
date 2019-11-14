import sys
sys.path.append('../Pieces')
import piece as PIECE

class Square:

    def __init__(self):
        """
        Define Square Class Variables
        """
        self.piece = PIECE.Piece()



    def copy(self):
        """
        Creates a copy of the square
        :return: A copy of the square
        """
        s = Square()
        s.piece = self.piece.copy()
        return s



    def has_piece(self):
        """
        Checks to see if the square has a piece on it
        :return: bool Whether or not square has a piece
        """
        if self.piece.name == 'null piece':
            return False
        else:
            return True



if __name__ == '__main__':
    s = Square()
    print("Square has", s.piece.name, "on it")
