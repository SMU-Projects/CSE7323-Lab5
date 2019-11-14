import sys
sys.path.append('../Pieces')
import piece as PIECE

class Square:

    def __init__(self):
        self.piece = PIECE.Piece()

    def copy(self):
        s = Square()
        s.piece = self.piece.copy()
        return s

if __name__ == '__main__':
    s = Square()
    print("Square has", s.piece.name, "on it")
