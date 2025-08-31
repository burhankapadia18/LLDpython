"""
Unequal Expense Split Module

This module defines the UnequalExpenseSplit class which implements the validation
strategy for unequal expense splitting. In unequal splitting, participants can owe
different amounts as long as the total adds up to the expense amount.

The UnequalExpenseSplit class validates that the sum of all split amounts equals
the total expense amount, but allows individual amounts to differ.
"""

from typing import List
from expense.split.split import Split
from expense.split.expense_split import ExpenseSplit


class UnequalExpenseSplit(ExpenseSplit):
    """
    Implementation of unequal expense split validation strategy.
    
    This class validates that an expense is split unequally among participants.
    Each participant can owe different amounts, but the sum of all split amounts
    must equal the total expense amount.
    """

    def validate_split_request(self, split_list: List[Split], total_amount: float) -> None:
        """
        Validate that the expense split amounts sum to the total amount.
        
        This method ensures that the sum of all split amounts equals the total
        expense amount. Individual amounts can differ, but the total must be correct.
        
        Args:
            split_list: List of Split objects representing the expense division
            total_amount: The total amount of the expense to be validated
            
        Raises:
            Exception: If the split amounts don't sum to total_amount
        """
        pass