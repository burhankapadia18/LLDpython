"""
User Expense Balance Sheet Module

This module defines the UserExpenseBalanceSheet class which maintains the complete
financial summary for a user in the Splitwise system. It tracks all expenses,
payments, and balances with other users.

The UserExpenseBalanceSheet provides a comprehensive view of a user's financial
position within the Splitwise application, including their total expenses,
payments made, amounts owed, and amounts to be received.
"""

from balance import Balance
from typing import Dict

class UserExpenseBalanceSheet:
    """
    Represents the complete balance sheet for a user in the Splitwise system.
    
    This class maintains a comprehensive financial summary for a user, including:
    - Total expenses incurred by the user
    - Total payments made by the user
    - Total amounts owed to other users
    - Total amounts to be received from other users
    - Detailed balance breakdown with each other user
    
    Attributes:
        user_vs_balance: Dictionary mapping user IDs to Balance objects
        total_your_expense: Total expenses incurred by this user
        total_payment: Total payments made by this user
        total_you_owe: Total amount this user owes to others
        total_you_get_back: Total amount this user should receive from others
    """

    user_vs_balance: Dict[str, Balance]
    total_your_expense: float
    total_payment: float
    total_you_owe: float
    total_you_get_back: float

    def __init__(self):
        """
        Initialize a new UserExpenseBalanceSheet with zero values.
        
        Creates a balance sheet with all financial totals set to 0
        and an empty dictionary for tracking balances with other users.
        """
        self.user_vs_balance = {}
        self.total_your_expense = 0
        self.total_you_owe = 0
        self.total_you_get_back = 0
        self.total_payment = 0

    def get_user_vs_balance(self) -> Dict[str, Balance]:
        """
        Get the dictionary of balances with other users.
        
        Returns:
            Dict[str, Balance]: Dictionary mapping user IDs to Balance objects
        """
        return self.user_vs_balance

    def get_total_your_expense(self) -> float:
        """
        Get the total expenses incurred by this user.
        
        Returns:
            float: Total amount of expenses incurred by the user
        """
        return self.total_your_expense
    
    def set_total_your_expense(self, total_your_expense: float) -> None:
        """
        Set the total expenses incurred by this user.
        
        Args:
            total_your_expense: The new total expense amount
        """
        self.total_your_expense = total_your_expense

    def get_total_you_owe(self) -> float:
        """
        Get the total amount this user owes to others.
        
        Returns:
            float: Total amount owed to other users
        """
        return self.total_you_owe

    def set_total_you_owe(self, total_you_owe: float) -> None:
        """
        Set the total amount this user owes to others.
        
        Args:
            total_you_owe: The new total amount owed
        """
        self.total_you_owe = total_you_owe

    def get_total_you_get_back(self) -> float:
        """
        Get the total amount this user should receive from others.
        
        Returns:
            float: Total amount to be received from other users
        """
        return self.total_you_get_back

    def set_total_you_get_back(self, total_you_get_back: float) -> None:
        """
        Set the total amount this user should receive from others.
        
        Args:
            total_you_get_back: The new total amount to be received
        """
        self.total_you_get_back = total_you_get_back

    def get_total_payment(self) -> float:
        """
        Get the total payments made by this user.
        
        Returns:
            float: Total amount of payments made by the user
        """
        return self.total_payment

    def set_total_payment(self, total_payment: float) -> None:
        """
        Set the total payments made by this user.
        
        Args:
            total_payment: The new total payment amount
        """
        self.total_payment = total_payment
