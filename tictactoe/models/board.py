"""
Board module for TicTacToe game.

This module implements the game board functionality, including piece placement,
board state management, and board display.
"""

from typing import List, Optional
from .playing_piece.piece import Piece

class Board:
    """
    A class representing the TicTacToe game board.
    
    This class manages the game board state, including piece placement,
    free cell tracking, and board display.
    
    Attributes:
        size (int): The size of the board (e.g., 3 for 3x3)
        board (List[List[Optional[Piece]]]): 2D list representing the game board
    """
    size: int
    board: List[List[Optional[Piece]]]
    
    def __init__(self, size: int) -> None:
        """
        Initialize a new game board.

        Args:
            size (int): The size of the board (e.g., 3 for 3x3)
        """
        self.size = size
        # Initialize empty board with None values
        self.board = [[None for j in range(self.size)] for i in range(self.size)]
    
    
    def add_piece(self, row: int, column: int, playingPiece: Piece) -> bool:
        """
        Attempt to add a playing piece to the board.

        Args:
            row (int): The row where the piece should be placed
            column (int): The column where the piece should be placed
            playingPiece (Piece): The piece to be placed

        Returns:
            bool: True if the piece was successfully placed, False if the position was occupied
        """
        # Check if the position is already occupied
        if self.board[row][column] != None:
            return False
        
        # Place the piece
        self.board[row][column] = playingPiece
        return True
    
    
    def get_free_cells(self) -> list:
        """
        Get a list of all free (unoccupied) cells on the board.

        Returns:
            list: List of [row, column] coordinates for all free cells
        """
        free_cells = []

        # Iterate through the board to find empty cells
        for i in range(self.size):
            for j in range(self.size):
                if self.board[i][j] is None:
                    free_cells.append([i, j])

        return free_cells
    
    
    def print_board(self) -> None:
        """
        Print the current state of the board to the console.
        
        The board is printed with pieces represented by their values
        and empty cells represented by spaces.
        """
        # Print each row of the board
        for i in range(self.size):
            for j in range(self.size):
                # Print piece value if cell is occupied, space if empty
                if self.board[i][j] is not None:
                   print(f"{self.board[i][j].piece_type.value}   ", end="")
                else:
                    print("    ", end="")
                print(" | ", end="")
            print()
