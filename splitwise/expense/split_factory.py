"""
Split Factory Module

This module defines the SplitFactory class which creates appropriate split objects
based on the split type. It implements the Factory pattern to provide the correct
split validation strategy for different types of expense splitting.

The SplitFactory supports different split types including EQUAL, UNEQUAL, and PERCENTAGE,
and returns the appropriate split object for validation and processing.
"""

from expense.split.equal_expense_split import EqualExpenseSplit
from expense.split.expense_split import ExpenseSplit
from expense.split.percentage_expense_split import PercentageExpenseSplit
from expense.split.unequal_expense_split import UnequalExpenseSplit
from expense.expense_split_type import ExpenseSplitType

class SplitFactory:
    """
    Factory class for creating split objects based on split type.
    
    This class implements the Factory pattern to create the appropriate
    split validation object based on the type of expense splitting required.
    It supports EQUAL, UNEQUAL, and PERCENTAGE split types.
    """

    def get_split_object(self, split_type: ExpenseSplitType) -> ExpenseSplit:
        """
        Get the appropriate split object based on the split type.
        
        Creates and returns the correct split validation object based on
        the specified split type. Each split type has its own validation logic.
        
        Args:
            split_type: The type of split (EQUAL, UNEQUAL, PERCENTAGE)
            
        Returns:
            ExpenseSplit: The appropriate split validation object, or None if type is not supported
        """
        if split_type == ExpenseSplitType.EQUAL:
            return EqualExpenseSplit()
        elif split_type == ExpenseSplitType.UNEQUAL:
            return UnequalExpenseSplit()
        elif split_type == ExpenseSplitType.PERCENTAGE:
            return PercentageExpenseSplit()
        else:
            return None
