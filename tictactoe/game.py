"""
TicTacToe Game Implementation

This module implements the core game logic for a TicTacToe game.
It handles player turns, board state management, and win condition checking.
"""

from typing import Deque, List
from collections import deque
from models.player import Player
from models.board import Board
from models.playing_piece.piece import PieceType


class TicTacToeGame:
    """
    A class representing a TicTacToe game instance.
    
    This class manages the game state, including the game board and player turns.
    It handles the main game loop and win condition checking.
    
    Attributes:
        players (Deque[Player]): A queue of players taking turns
        game_board (Board): The game board instance
    """
    players: Deque[Player]
    game_board: Board

    def __init__(self, size: int, players: List[Player]) -> None:
        """
        Initialize a new TicTacToe game.

        Args:
            size (int): The size of the game board (e.g., 3 for 3x3)
            players (List[Player]): List of players participating in the game
        """
        self.game_board = Board(size)
        self.players = deque()
        for player in players:
            self.players.append(player)

    
    def start_game(self) -> str:
        """
        Start and run the TicTacToe game.

        This method manages the main game loop, handling player turns,
        board updates, and win condition checking.

        Returns:
            str: The name of the winning player or "tie" if the game ends in a draw
        """
        no_winner = True
        while no_winner:
            # Get the current player's turn
            player_turn = self.players.popleft()

            # Display current board state
            self.game_board.print_board()
            freeSpaces = self.game_board.get_free_cells()
            
            # Check for draw condition
            if len(freeSpaces) == 0:
                no_winner = False
                continue

            # Get player's move
            s = input(f"Player:{player_turn.name} Enter row,column: ")
            values = s.split(',')
            row = int(values[0])
            col = int(values[1])

            # Attempt to place the piece
            piece_added_successfully = self.game_board.add_piece(row, col, player_turn.playing_piece)
            if not piece_added_successfully:
                print("Incorrect position chosen, try again")
                self.players.appendleft(player_turn)
                continue
            
            # Add player back to queue for next turn
            self.players.append(player_turn)

            # Check for win condition
            winner = self.is_there_winner(row, col, player_turn.playing_piece.piece_type)
            if winner:
                return player_turn.name

        return "tie"
    

    def is_there_winner(self, row: int, column: int, piece_type: PieceType) -> bool:
        """
        Check if the current move results in a win.

        This method checks all possible winning combinations:
        - Row completion
        - Column completion
        - Diagonal completion
        - Anti-diagonal completion

        Args:
            row (int): The row where the last piece was placed
            column (int): The column where the last piece was placed
            piece_type (PieceType): The type of piece that was placed

        Returns:
            bool: True if there is a winner, False otherwise
        """
        # Initialize win condition flags
        rowMatch = True
        columnMatch = True
        diagonalMatch = True
        antiDiagonalMatch = True

        # Check row completion
        for i in range(self.game_board.size):
            if self.game_board.board[row][i] == None or self.game_board.board[row][i].piece_type != piece_type:
                rowMatch = False

        # Check column completion
        for i in range(self.game_board.size):
            if self.game_board.board[i][column] == None or self.game_board.board[i][column].piece_type != piece_type:
                columnMatch = False

        # Check diagonal completion (top-left to bottom-right)
        i, j = 0, 0
        while i < self.game_board.size:
            if self.game_board.board[i][j] == None or self.game_board.board[i][j].piece_type != piece_type:
                diagonalMatch = False
            i += 1
            j += 1

        # Check anti-diagonal completion (top-right to bottom-left)
        i, j = 0, self.game_board.size - 1
        while i < self.game_board.size:
            if self.game_board.board[i][j] == None or self.game_board.board[i][j].piece_type != piece_type:
                antiDiagonalMatch = False
            i += 1
            j -= 1

        return rowMatch or columnMatch or diagonalMatch or antiDiagonalMatch
