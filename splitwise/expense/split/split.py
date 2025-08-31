"""
Split Module

This module defines the Split class which represents how an expense is divided
among users in the Splitwise system. Each split contains information about
a specific user and how much they owe for a particular expense.

The Split class is a fundamental building block for expense splitting, representing
the relationship between a user and their portion of an expense.
"""

from user.user import User


class Split:
    """
    Represents how an expense is split for a specific user.
    
    A split defines the relationship between a user and their portion of an expense.
    It contains information about which user is involved and how much they owe
    for the expense.
    
    Attributes:
        user: The user who is part of this split
        amount_owe: The amount this user owes for the expense
    """

    user: User
    amount_owe: float

    def __init__(self, user: User, amount_owe: float):
        """
        Initialize a new Split with the specified user and amount.
        
        Creates a split object that associates a user with their portion
        of an expense.
        
        Args:
            user: The user who is part of this split
            amount_owe: The amount this user owes for the expense
        """
        self.user = user
        self.amount_owe = amount_owe

    def get_user(self) -> User:
        """
        Get the user associated with this split.
        
        Returns:
            User: The user who is part of this split
        """
        return self.user

    def set_user(self, user: User) -> None:
        """
        Set the user associated with this split.
        
        Args:
            user: The new user to associate with this split
        """
        self.user = user

    def get_amount_owe(self) -> float:
        """
        Get the amount this user owes for the expense.
        
        Returns:
            float: The amount this user owes
        """
        return self.amount_owe

    def set_amount_owe(self, amount_owe: float) -> None:
        """
        Set the amount this user owes for the expense.
        
        Args:
            amount_owe: The new amount this user owes
        """
        self.amount_owe = amount_owe
