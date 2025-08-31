"""
Expense Controller Module

This module defines the ExpenseController class which manages all expense-related operations
in the Splitwise system. It handles expense creation, validation, and balance sheet updates.

The ExpenseController serves as the central point for expense management, coordinating
between expense creation, split validation, and balance sheet updates.
"""

from balance_sheet_controller import BalanceSheetController
from expense.split.split import Split
from expense.expense_split_type import ExpenseSplitType
from user.user import User
from expense.split_factory import SplitFactory
from expense.expense import Expense
from typing import List


class ExpenseController:
    """
    Controller class for managing expenses in the Splitwise system.
    
    This class handles the creation and management of expenses, including:
    - Creating new expenses with proper validation
    - Coordinating with split factories for split validation
    - Updating balance sheets when expenses are created
    - Managing the relationship between expenses and balance sheets
    
    Attributes:
        balance_sheet_controller: Controller for managing balance sheet updates
    """

    balance_sheet_controller: BalanceSheetController

    def __init__(self):
        """
        Initialize the ExpenseController with a balance sheet controller.
        
        Creates a new ExpenseController instance with a BalanceSheetController
        to handle balance sheet updates when expenses are created.
        """
        self.balance_sheet_controller = BalanceSheetController()

    def create_expense(self, expense_id: str, description: str, expense_amount: float,
                                 split_details: List[Split], split_type: ExpenseSplitType, paid_by_user: User):
        """
        Create a new expense with proper validation and balance sheet updates.
        
        This method performs the complete expense creation workflow:
        1. Gets the appropriate split object based on split type
        2. Validates the split request to ensure it's valid
        3. Creates the expense object
        4. Updates all relevant balance sheets
        
        Args:
            expense_id: Unique identifier for the expense
            description: Description of what the expense was for
            expense_amount: Total amount of the expense
            split_details: List of Split objects defining how the expense is divided
            split_type: Type of split used (EQUAL, UNEQUAL, PERCENTAGE)
            paid_by_user: The user who paid for the expense
            
        Returns:
            Expense: The created expense object
        """
        # Get the appropriate split object and validate the split request
        expense_split = SplitFactory().get_split_object(split_type)
        expense_split.validate_split_request(split_details, expense_amount)

        # Create the expense object
        expense = Expense(expense_id, expense_amount, description, paid_by_user, split_type, split_details)

        # Update all relevant balance sheets
        self.balance_sheet_controller.update_user_expense_balance_sheet(paid_by_user, split_details, expense_amount)

        return expense
