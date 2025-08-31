"""
Expense Module

This module defines the Expense class which represents an expense in the Splitwise system.
An expense is a financial transaction that is shared among multiple users with a specific split type.

The Expense class contains all the information about a financial transaction including
who paid for it, how much it cost, how it should be split among users, and the split details.
"""

from expense.split.split import Split
from user.user import User
from expense.expense_split_type import ExpenseSplitType
from typing import List

class Expense:
    """
    Represents an expense in the Splitwise system.
    
    An expense is a financial transaction that involves multiple users. It contains
    information about who paid for the expense, how much it cost, how it should be
    split among users, and the specific split details for each user.
    
    Attributes:
        expense_id: Unique identifier for the expense
        description: Description of what the expense was for
        expense_amount: Total amount of the expense
        paid_by_user: The user who paid for the expense
        split_type: Type of split used (EQUAL, UNEQUAL, PERCENTAGE)
        split_details: List of Split objects defining how the expense is divided
    """

    expense_id: str
    description: str
    expense_amount: float
    paid_by_user: User
    split_type: ExpenseSplitType
    split_details: List[Split]

    def __init__(self, expense_id: str, expense_amount: float, description: str,
                   paid_by_user: User, split_type: ExpenseSplitType, split_details: List[Split]):
        """
        Initialize a new Expense with the specified details.
        
        Creates an expense with all the necessary information including the amount,
        description, who paid for it, how it should be split, and the split details.
        
        Args:
            expense_id: Unique identifier for the expense
            expense_amount: Total amount of the expense
            description: Description of what the expense was for
            paid_by_user: The user who paid for the expense
            split_type: Type of split used (EQUAL, UNEQUAL, PERCENTAGE)
            split_details: List of Split objects defining how the expense is divided
        """
        self.expense_id = expense_id
        self.expense_amount = expense_amount
        self.description = description
        self.paid_by_user = paid_by_user
        self.split_type = split_type
        self.split_details = split_details
        self.split_details.extend(split_details)
