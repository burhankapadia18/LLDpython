from abc import ABC
from enum import Enum

class PieceType(Enum):
    X = 'X'
    O = 'O'

class Piece(ABC):
    piece_type: PieceType
    
    def __init__(self, piece_type: PieceType) -> None:
        self.piece_type = piece_type