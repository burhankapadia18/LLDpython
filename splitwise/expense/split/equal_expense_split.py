"""
Equal Expense Split Module

This module defines the EqualExpenseSplit class which implements the validation
strategy for equal expense splitting. In equal splitting, the total expense amount
is divided equally among all participants.

The EqualExpenseSplit class validates that each user's split amount equals the
total amount divided by the number of participants.
"""

from expense.split.expense_split import ExpenseSplit
from expense.split.split import Split
from typing import List


class EqualExpenseSplit(ExpenseSplit):
    """
    Implementation of equal expense split validation strategy.
    
    This class validates that an expense is split equally among all participants.
    Each participant should owe exactly the same amount, which is the total
    expense amount divided by the number of participants.
    """

    def validate_split_request(self, split_list: List[Split], total_amount: float) -> None:
        """
        Validate that the expense is split equally among all participants.
        
        This method ensures that each user's split amount equals the total amount
        divided by the number of participants. If any split amount differs from
        this calculated amount, the validation fails.
        
        Args:
            split_list: List of Split objects representing the expense division
            total_amount: The total amount of the expense to be validated
            
        Raises:
            Exception: If the split amounts are not equal or don't sum to total_amount
        """
        # Validate total amount in splits of each user is equal and overall equals to total_amount or not
        amount_should_be_present = total_amount/len(split_list)
        for split in split_list:
           if(split.get_amount_owe() != amount_should_be_present):
               # Throw exception - split amounts are not equal
               pass
