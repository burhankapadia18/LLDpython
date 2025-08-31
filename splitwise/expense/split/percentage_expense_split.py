"""
Percentage Expense Split Module

This module defines the PercentageExpenseSplit class which implements the validation
strategy for percentage-based expense splitting. In percentage splitting, each
participant owes a percentage of the total expense amount.

The PercentageExpenseSplit class validates that the percentages sum to 100% and
that the calculated amounts match the split details.
"""

from expense.split.expense_split import ExpenseSplit
from expense.split.split import Split
from typing import List


class PercentageExpenseSplit(ExpenseSplit):
    """
    Implementation of percentage-based expense split validation strategy.
    
    This class validates that an expense is split based on percentages among participants.
    Each participant owes a percentage of the total amount, and the sum of all
    percentages should equal 100%.
    """

    def validate_split_request(self, split_list: List[Split], total_amount: float) -> None:
        """
        Validate that the expense is split based on valid percentages.
        
        This method ensures that the split amounts represent valid percentages
        of the total expense amount. The validation would typically check that
        percentages sum to 100% and that calculated amounts match the split details.
        
        Args:
            split_list: List of Split objects representing the expense division
            total_amount: The total amount of the expense to be validated
            
        Raises:
            Exception: If the percentage split is invalid
        """
        pass
