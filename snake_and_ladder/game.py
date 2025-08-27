"""
Snake and Ladder Game - Core Game Logic

This module contains the main Game class that orchestrates the entire Snake and Ladder game.
It manages the game state, player turns, dice rolling, movement, and win conditions.

The Game class coordinates between the Board, Dice, and Player components to create
a complete gameplay experience. It handles the main game loop, player turn management,
position updates, and win condition checking.
"""

from board import Board
from dice import Dice
from player import Player

class Game:
    """
    Main game controller class that manages the Snake and Ladder game.
    
    This class orchestrates all game components including the board, dice, players,
    and game flow. It handles player turns, dice rolling, position updates,
    snake/ladder effects, and win conditions.
    
    Attributes:
        board (Board): The game board containing cells with snakes and ladders
        dice (Dice): The dice object used for rolling
        players_list (list[Player]): List of players participating in the game
        winner (Player | None): The winning player, None if game is ongoing
    """
    
    board: Board
    dice: Dice
    players_list: list[Player]
    winner: Player | None

    def __init__(self) -> None:
        """
        Initialize a new Snake and Ladder game.
        
        Sets up the game board with snakes and ladders, creates dice,
        initializes players, and prepares the game state.
        """
        self.__initialize_game()

    def __initialize_game(self) -> None:
        """
        Initialize all game components.
        
        Creates a 10x10 board with 5 snakes and 4 ladders, initializes
        a single dice, sets winner to None, and adds players to the game.
        """
        self.board = Board(10, 5,4)
        self.dice = Dice(1)
        self.winner = None
        self.__add_players()

    def __add_players(self) -> None:
        """
        Add players to the game.
        
        Creates two players (p1 and p2) with initial position 0
        and adds them to the players list.
        """
        self.players_list = []
        player1 = Player("p1", 0)
        player2 = Player("p2", 0)
        self.players_list.append(player1)
        self.players_list.append(player2)

    def startGame(self) -> None:
        """
        Start the main game loop.
        
        Runs the game until a winner is determined. For each turn:
        1. Determines whose turn it is
        2. Rolls the dice
        3. Updates player position
        4. Checks for snake/ladder effects
        5. Checks for win condition
        
        The game continues until a player reaches or exceeds the final position.
        """
        while self.winner is None:

            # check whose turn now
            player_turn = self.__find_player_turn()
            print("player turn is: " + player_turn.id + " current position is: " + str(player_turn.current_position))

            # roll the dice
            dice_numbers = self.dice.roll_dice()

            # get the new position
            player_new_position = player_turn.current_position + dice_numbers
            player_new_position = self.__jump_check(player_new_position)
            player_turn.current_position = player_new_position

            print("player turn is:" + player_turn.id + " new Position is: " + str(player_new_position))
            # check for winning condition
            if player_new_position >= len(self.board.cells) * len(self.board.cells)-1:
                self.winner = player_turn


        print("WINNER IS:" + self.winner.id)


    def __find_player_turn(self) -> Player:
        """
        Determine which player's turn it is using round-robin scheduling.
        
        Removes the first player from the list and adds them to the end,
        effectively rotating the turn order.
        
        Returns:
            Player: The player whose turn it is
        """
        player_turns = self.players_list.pop(0)
        self.players_list.append(player_turns)
        return player_turns

    def __jump_check(self, player_new_position) -> int:
        """
        Check if the player's new position has a snake or ladder.
        
        If the position contains a jump (snake or ladder), the player
        is moved to the end position of that jump. Snakes move players
        down (start > end), while ladders move players up (start < end).
        
        Args:
            player_new_position (int): The position to check for jumps
            
        Returns:
            int: The final position after applying any snake/ladder effects
        """
        if player_new_position > len(self.board.cells) * len(self.board.cells)-1 :
            return player_new_position

        cell = self.board.get_cell(player_new_position)
        if cell.jump is not None and cell.jump.start == player_new_position:
            jump_by = "ladder" if cell.jump.start < cell.jump.end else "snake"
            print("jump done by: " + jump_by)
            return cell.jump.end
        return player_new_position
