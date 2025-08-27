"""
Snake and Ladder Game - Player Management

This module contains the Player class that represents a player in the
Snake and Ladder game. Each player has a unique identifier and tracks
their current position on the game board.

The Player class is a simple data structure that maintains player state
and can be extended to include additional player-specific information.
"""

class Player:
    """
    Represents a player in the Snake and Ladder game.
    
    Each player has a unique identifier and tracks their current position
    on the game board. The position starts at 0 and increases as the
    player moves across the board.
    
    Attributes:
        id (str): Unique identifier for the player
        current_position (int): Current position of the player on the board
    """
    
    id: str
    current_position: int

    def __init__(self, id: str, current_position: int) -> None:
        """
        Initialize a new player with the specified ID and starting position.
        
        Args:
            id (str): Unique identifier for the player
            current_position (int): Starting position on the board (typically 0)
        """
        self.id = id
        self.current_position = current_position
