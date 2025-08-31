"""
Balance Module

This module defines the Balance class which represents the financial balance
between two users in the Splitwise system. It tracks amounts owed and amounts
to be received between any pair of users.

The Balance class is used to maintain the relationship between users and
track their mutual financial obligations.
"""

class Balance:
    """
    Represents the balance between two users in the Splitwise system.
    
    This class tracks the financial relationship between any pair of users,
    maintaining both the amount one user owes to another and the amount
    they should receive from the other user.
    
    Attributes:
        amount_owe: The amount this user owes to the other user
        amount_get_back: The amount this user should receive from the other user
    """

    amount_owe: float
    amount_get_back: float

    def __init__(self):
        """
        Initialize a new Balance instance with zero amounts.
        
        Creates a balance object with both owed and receivable amounts
        set to 0.0, representing a neutral balance state.
        """
        self.amount_owe = 0.0
        self.amount_get_back = 0.0

    def get_amount_owe(self) -> float:
        """
        Get the amount this user owes to the other user.
        
        Returns:
            float: The amount owed to the other user
        """
        return self.amount_owe

    def set_amount_owe(self, amount_owe: float) -> None:
        """
        Set the amount this user owes to the other user.
        
        Args:
            amount_owe: The new amount owed to the other user
        """
        self.amount_owe = amount_owe

    def get_amount_get_back(self) -> float:
        """
        Get the amount this user should receive from the other user.
        
        Returns:
            float: The amount to be received from the other user
        """
        return self.amount_get_back

    def set_amount_get_back(self, amount_get_back: float) -> None:
        """
        Set the amount this user should receive from the other user.
        
        Args:
            amount_get_back: The new amount to be received from the other user
        """
        self.amount_get_back = amount_get_back
