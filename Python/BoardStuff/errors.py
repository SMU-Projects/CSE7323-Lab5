class UndefinedPieceColor(Exception):
    """
    Raised when the color of the piece is unknown
    """
    def __init__(self, color, name):
        print("Error: The specified color \"", color, "\" for piece \"", name, "\" is undefined.")

