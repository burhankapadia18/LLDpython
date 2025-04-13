from .piece import Piece, PieceType

class PieceO(Piece):
    
    def __init__(self) -> None:
        super().__init__(PieceType.O)