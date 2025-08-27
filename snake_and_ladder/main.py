"""
Snake and Ladder Game - Main Entry Point

This module serves as the entry point for the Snake and Ladder game.
It initializes and starts the game by creating a Game instance and calling startGame().

The game follows the classic Snake and Ladder rules where players roll dice,
move across a board, and encounter snakes (that move them down) and ladders
(that move them up). The first player to reach the final position wins.
"""

from game import Game

def main():
    """
    Main function that initializes and starts the Snake and Ladder game.
    
    Creates a new Game instance and calls the startGame method to begin
    the gameplay loop.
    """
    game_obj = Game()
    game_obj.startGame()


if __name__ == "__main__":
    main()
