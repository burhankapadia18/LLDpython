from typing import List, Optional
from .playing_piece.piece import Piece

class Board():
    size: int
    board: List[List[Optional[Piece]]]
    
    def __init__(self, size: int) -> None:
        self.size = size
        self.board = [[None for j in range(self.size)] for i in range(self.size)]
    
    
    def add_piece(self, row: int, column: int, playingPiece: Piece) -> bool:

        if self.board[row][column] != None:
            return False
        
        self.board[row][column] = playingPiece
        return True
    
    
    def get_free_cells(self) -> list:
        free_cells = []

        for i in range(self.size):
            for j in range(self.size):
                if self.board[i][j] is None:
                    free_cells.append([i, j])

        return free_cells
    
    
    def print_board(self) -> None:
        
        for i in range(self.size):
            for j in range(self.size):
                if self.board[i][j] is not None:
                   print(f"{self.board[i][j].piece_type.value}   ", end="")
                else:
                    print("    ", end="")
                print(" | ", end="")
            print()
