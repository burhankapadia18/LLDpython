"""
Snake and Ladder Game - Board Management

This module contains the Board class that represents the game board for Snake and Ladder.
The board is a 2D grid of cells, some of which contain snakes or ladders that affect
player movement.

The Board class handles board initialization, cell management, and the placement
of snakes and ladders at random positions on the board.
"""

import random
from cell import Cell
from jump import Jump
from typing import List

class Board:
    """
    Represents the game board for Snake and Ladder.
    
    The board is a 2D grid where each cell may contain a snake or ladder.
    Snakes move players down (from higher to lower position), while ladders
    move players up (from lower to higher position).
    
    Attributes:
        cells (List[List[Cell]]): 2D grid of cells representing the board
    """
    
    cells: List[List[Cell]]

    def __init__(self, board_size: int, number_of_snakes: int, number_of_ladders: int) -> None:
        """
        Initialize the game board with specified dimensions and features.
        
        Creates a board of the given size and randomly places the specified
        number of snakes and ladders on the board.
        
        Args:
            board_size (int): The size of the board (creates board_size x board_size grid)
            number_of_snakes (int): Number of snakes to place on the board
            number_of_ladders (int): Number of ladders to place on the board
        """
        self.__initialize_cells(board_size)
        self.__add_snakes_ladders(number_of_snakes, number_of_ladders)


    def __initialize_cells(self, board_size: int) -> None:
        """
        Initialize the board with empty cells.
        
        Creates a 2D grid of Cell objects with the specified board size.
        All cells start without any snakes or ladders.
        
        Args:
            board_size (int): The size of the board (creates board_size x board_size grid)
        """
        self.cells = [[None for _ in range(board_size)] for _ in range(board_size)]
        for i in range(0, board_size):
            for j in range(0, board_size):
                cell_obj = Cell()
                self.cells[i][j] = cell_obj
        

    def  __add_snakes_ladders(self, number_of_snakes: int, number_of_ladders: int) -> None:
        """
        Add snakes and ladders to the board at random positions.
        
        Places the specified number of snakes and ladders on the board.
        Snakes are placed so that the head (start) is higher than the tail (end),
        while ladders are placed so that the start is lower than the end.
        
        Args:
            number_of_snakes (int): Number of snakes to place on the board
            number_of_ladders (int): Number of ladders to place on the board
        """
        while number_of_snakes > 0:
            snake_head = random.randint(1, len(self.cells)*len(self.cells)-1)
            snake_tail = random.randint(1, len(self.cells)*len(self.cells)-1)
            if snake_tail >= snake_head:
                continue

            snake_obj = Jump(snake_head, snake_tail)
            cell = self.get_cell(snake_head)
            cell.jump = snake_obj

            number_of_snakes = number_of_snakes - 1

        while number_of_ladders > 0:
            ladder_start = random.randint(1, len(self.cells)*len(self.cells)-1)
            ladder_end = random.randint(1, len(self.cells)*len(self.cells)-1)
            if ladder_start >= ladder_end:
                continue

            ladder_obj = Jump(ladder_start, ladder_end)

            cell = self.get_cell(ladder_start)
            cell.jump = ladder_obj

            number_of_ladders = number_of_ladders - 1


    def get_cell(self, position: int) -> Cell:
        """
        Get the cell at a specific position on the board.
        
        Converts a 1D position to 2D coordinates and returns the corresponding cell.
        The board is traversed from bottom-left to top-right, starting from position 0.
        
        Args:
            position (int): The 1D position on the board (0 to board_size^2 - 1)
            
        Returns:
            Cell: The cell at the specified position
        """
        board_row = position // len(self.cells)
        board_column = position % len(self.cells)
        return self.cells[board_row][board_column]
