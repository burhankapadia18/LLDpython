"""
Expense Split Module

This module defines the abstract ExpenseSplit class which serves as the base class
for all split validation strategies in the Splitwise system. It defines the interface
that all split types must implement.

The ExpenseSplit class uses the Strategy pattern to allow different validation
strategies for different types of expense splitting (EQUAL, UNEQUAL, PERCENTAGE).
"""

import abc
from typing import List
from expense.split.split import Split


class ExpenseSplit(abc.ABC):
    """
    Abstract base class for expense split validation strategies.
    
    This class defines the interface that all split validation strategies must implement.
    It uses the Strategy pattern to allow different validation logic for different
    types of expense splitting.
    
    Subclasses must implement the validate_split_request method to provide
    specific validation logic for their split type.
    """

    @abc.abstractmethod
    def validate_split_request(self, split_list: List[Split], total_amount: float):
        """
        Validate a split request based on the specific split strategy.
        
        This abstract method must be implemented by subclasses to provide
        specific validation logic for their split type. The validation ensures
        that the split details are consistent with the split type and total amount.
        
        Args:
            split_list: List of Split objects representing the expense division
            total_amount: The total amount of the expense to be validated
        """
        pass    
