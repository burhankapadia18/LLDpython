"""
X piece implementation for TicTacToe game.

This module implements the X piece for the TicTacToe game.
It extends the base Piece class with the X piece type.
"""

from .piece import Piece, PieceType

class PieceX(Piece):
    """
    Class representing the X piece in the TicTacToe game.
    
    This class extends the base Piece class and initializes it
    with the X piece type.
    """
    
    def __init__(self) -> None:
        """
        Initialize a new X piece.
        
        This constructor calls the parent class constructor with
        the PieceType.X enum value.
        """
        super().__init__(PieceType.X)