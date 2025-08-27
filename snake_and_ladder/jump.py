"""
Snake and Ladder Game - Jump Management

This module contains the Jump class that represents snakes and ladders
on the game board. A jump defines a connection between two positions
on the board that affects player movement.

The Jump class is used to represent both snakes (which move players down)
and ladders (which move players up) by defining start and end positions.
"""

class Jump:
    """
    Represents a jump (snake or ladder) on the game board.
    
    A jump connects two positions on the board. When a player lands on
    the start position, they are moved to the end position.
    
    - For ladders: start < end (moves player up)
    - For snakes: start > end (moves player down)
    
    Attributes:
        start (int): Starting position of the jump
        end (int): Ending position of the jump
    """
    
    start: int
    end: int

    def __init__(self, start: int, end: int):
        """
        Initialize a jump with start and end positions.
        
        Args:
            start (int): Starting position of the jump
            end (int): Ending position of the jump
        """
        self.start = start
        self.end = end
