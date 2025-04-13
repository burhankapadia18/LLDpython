from .piece import Piece, PieceType

class PieceX(Piece):
    
    def __init__(self) -> None:
        super().__init__(PieceType.X)