import sys
sys.path.append('../Pieces')
import piece as PIECE

class UndefinedPieceColor(Exception):
    """
    Raised when the color of the piece is unknown
    """
    def __init__(self, piece):
        print("Error: The specified color \"", piece.color, "\" for piece \"", piece.name, "\" is undefined.")

