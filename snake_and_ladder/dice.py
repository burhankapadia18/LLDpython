"""
Snake and Ladder Game - Dice Management

This module contains the Dice class that handles dice rolling functionality
for the Snake and Ladder game. It supports rolling multiple dice and
calculating the total sum of the rolls.

The Dice class provides a simple interface for generating random numbers
that determine how many positions a player moves on the board.
"""

import random

class Dice:
    """
    Represents dice used in the Snake and Ladder game.
    
    This class handles dice rolling functionality, supporting multiple dice
    and calculating the total sum of all dice rolls. Each die has values
    from 1 to 6.
    
    Attributes:
        dice_count (int): Number of dice to roll
        min (int): Minimum value on each die (1)
        max (int): Maximum value on each die (6)
    """
    
    dice_count: int
    min: int
    max: int

    def __init__(self, dice_count: int):
        """
        Initialize dice with the specified number of dice.
        
        Args:
            dice_count (int): Number of dice to use for rolling
        """
        self.min = 1
        self.max = 6
        self.dice_count = dice_count


    def  roll_dice(self) -> int:
        """
        Roll all dice and return the total sum.
        
        Rolls the specified number of dice, each with values from 1 to 6,
        and returns the sum of all dice values.
        
        Returns:
            int: The total sum of all dice rolls
        """
        total_sum = 0
        dice_used = 0

        while dice_used < self.dice_count:

            total_sum += random.randint(self.min, self.max+1)
            dice_used += dice_used
            dice_used += 1

        return total_sum
