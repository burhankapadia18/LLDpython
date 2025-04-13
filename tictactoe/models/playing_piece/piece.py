"""
Playing piece module for TicTacToe game.

This module defines the base piece class and piece types used in the game.
It provides an abstract base class for game pieces and an enumeration
for the different piece types (X and O).
"""

from abc import ABC
from enum import Enum

class PieceType(Enum):
    """
    Enumeration of possible piece types in the TicTacToe game.
    
    This enum defines the two possible piece types:
    - X: Represents the X piece
    - O: Represents the O piece
    """
    X = 'X'
    O = 'O'

class Piece(ABC):
    """
    Abstract base class for TicTacToe game pieces.
    
    This class serves as the base for all playing pieces in the game.
    It defines the common attributes and methods that all pieces must have.
    
    Attributes:
        piece_type (PieceType): The type of the piece (X or O)
    """
    piece_type: PieceType
    
    def __init__(self, piece_type: PieceType) -> None:
        """
        Initialize a new piece with the specified type.

        Args:
            piece_type (PieceType): The type of the piece (X or O)
        """
        self.piece_type = piece_type