import sys
sys.path.append('../Pieces')
import piece as PIECE

class Square:

    def __init__(self, row, col):
        """
        Define Square Class Variables
        :param row: row of chess square
        :param col: col of chess square
        """
        self.row = row
        self.col = col
        self.piece = PIECE.Piece()



    def copy(self):
        """
        Creates a copy of the square
        :return: A copy of the square
        """
        s = Square(self.row, self.col)
        s.row = self.row
        s.col = self.col
        s.piece = self.piece._copy()
        return s



    def set_piece(self, piece):
        """
        Sets a piece on the square
        :param piece: Piece to be set
        """
        piece.row = self.row
        piece.col = self.col
        self.piece = piece



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
    s = Square(0, 0)
    print("Square has", s.piece.name, "on it")
