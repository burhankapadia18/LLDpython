"""
O piece implementation for TicTacToe game.

This module implements the O piece for the TicTacToe game.
It extends the base Piece class with the O piece type.
"""

from .piece import Piece, PieceType

class PieceO(Piece):
    """
    Class representing the O piece in the TicTacToe game.
    
    This class extends the base Piece class and initializes it
    with the O piece type.
    """
    
    def __init__(self) -> None:
        """
        Initialize a new O piece.
        
        This constructor calls the parent class constructor with
        the PieceType.O enum value.
        """
        super().__init__(PieceType.O)