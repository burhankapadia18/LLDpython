"""
User Module

This module defines the User class which represents a user in the Splitwise system.
Each user has a unique identifier, name, and maintains their own expense balance sheet.

The User class serves as the core entity in the Splitwise application, representing
individual users who can participate in groups, create expenses, and track their
financial relationships with other users.
"""

from user_expense_balance_sheet import UserExpenseBalanceSheet


class User:
    """
    Represents a user in the Splitwise system.
    
    Each user has a unique identifier, display name, and maintains their own
    expense balance sheet to track financial relationships with other users.
    
    Attributes:
        user_id: Unique identifier for the user
        user_name: Display name of the user
        user_expense_balance_sheet: The user's personal expense balance sheet
    """

    user_id: str
    user_name: str
    user_expense_balance_sheet: UserExpenseBalanceSheet

    def __init__(self, id: str, user_name: str):
        """
        Initialize a new User with the given ID and name.
        
        Creates a user with a unique identifier and display name, and initializes
        their personal expense balance sheet to track financial relationships.
        
        Args:
            id: Unique identifier for the user
            user_name: Display name for the user
        """
        self.user_id = id
        self.user_name = user_name
        self.user_expense_balance_sheet = UserExpenseBalanceSheet()

    def get_user_id(self) -> str:
        """
        Get the unique identifier for this user.
        
        Returns:
            str: The user's unique identifier
        """
        return self.user_id

    def get_user_expense_balance_sheet(self) -> UserExpenseBalanceSheet:
        """
        Get the user's expense balance sheet.
        
        Returns:
            UserExpenseBalanceSheet: The user's personal balance sheet
        """
        return self.user_expense_balance_sheet
