"""
Main entry point for the TicTacToe game.

This module initializes the game components and starts the game.
It sets up two players with their respective pieces (X and O)
and creates a new game instance.
"""

from models.player import Player
from models.playing_piece.piece_o import PieceO
from models.playing_piece.piece_x import PieceX
from game import TicTacToeGame


def main():
    """
    Initialize and start a new TicTacToe game.
    
    This function:
    1. Creates two players with X and O pieces
    2. Initializes a 3x3 game board
    3. Starts the game and displays the winner
    """
    # Create playing pieces
    cross_piece = PieceX()
    player1 = Player("Player1", cross_piece)
    noughts_piece = PieceO()
    player2 = Player("Player2", noughts_piece)
    
    # Initialize and start the game
    game = TicTacToeGame(3, [player1, player2])
    print("game winner is: " + game.start_game())


if __name__ == "__main__":
    main()