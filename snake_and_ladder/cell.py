"""
Snake and Ladder Game - Cell Management

This module contains the Cell class that represents individual cells on the
Snake and Ladder game board. Each cell may contain a jump (snake or ladder)
that affects player movement when they land on it.

The Cell class serves as a container for jumps and can be extended to include
additional cell-specific properties or behaviors.
"""

from jump import Jump

class Cell:
    """
    Represents a single cell on the Snake and Ladder game board.
    
    Each cell can contain an optional jump (snake or ladder) that affects
    player movement. If a player lands on a cell with a jump, they are
    moved to the jump's end position.
    
    Attributes:
        jump (Jump | None): Optional jump (snake or ladder) on this cell
    """
    
    jump: Jump

    def __init__(self, jump: Jump = None):
        """
        Initialize a cell with an optional jump.
        
        Args:
            jump (Jump | None): Optional jump to place on this cell. 
                               Defaults to None for empty cells.
        """
        self.jump = jump
