"""
Player module for TicTacToe game.

This module implements the player functionality, including player attributes
and piece assignment.
"""

from .playing_piece.piece import Piece

class Player:
    """
    A class representing a player in the TicTacToe game.
    
    This class manages player information and their associated playing piece.
    
    Attributes:
        name (str): The name of the player
        playing_piece (Piece): The piece type assigned to the player (X or O)
    """
    name: str
    playing_piece: Piece
    
    def __init__(self, name: str, playing_piece: Piece) -> None:
        """
        Initialize a new player.

        Args:
            name (str): The name of the player
            playing_piece (Piece): The piece type assigned to the player
        """
        self.name = name
        self.playing_piece = playing_piece