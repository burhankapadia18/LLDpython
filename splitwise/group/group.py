"""
Group Module

This module defines the Group class which represents a group of users in the Splitwise system.
Groups allow users to organize expenses and share them among multiple members.

The Group class manages group members, expenses within the group, and provides
functionality to create expenses that are automatically split among group members.
"""

from expense.expense import Expense
from expense.expense_controller import ExpenseController
from expense.expense_split_type import ExpenseSplitType
from expense.split.split import Split
from user.user import User
from typing import List


class Group:
    """
    Represents a group of users in the Splitwise system.
    
    A group contains multiple users who can share expenses. The group manages
    its members, maintains a list of expenses, and provides functionality to
    create new expenses that are automatically split among group members.
    
    Attributes:
        group_id: Unique identifier for the group
        group_name: Display name of the group
        group_members: List of users who are members of this group
        expense_list: List of expenses created within this group
        expense_controller: Controller for managing expenses in this group
    """

    group_id: str
    group_name: str
    group_members: List[User]
    expense_list: List[Expense]
    expense_controller: ExpenseController

    def __init__(self):
        """
        Initialize a new Group with empty member and expense lists.
        
        Creates a new group with empty lists for members and expenses,
        and initializes an expense controller for managing group expenses.
        """
        self.group_members = []
        self.expense_list = []
        self.expense_controller = ExpenseController()

    def add_member(self, member: User):
        """
        Add a new member to the group.
        
        Adds the specified user to the list of group members.
        
        Args:
            member: The User object to add as a member
        """
        self.group_members.append(member)
    
    def get_group_id(self) -> str:
        """
        Get the unique identifier for this group.
        
        Returns:
            str: The group's unique identifier
        """
        return self.group_id

    def set_group_id(self, group_id: str):
        """
        Set the unique identifier for this group.
        
        Args:
            group_id: The new unique identifier for the group
        """
        self.group_id = group_id

    def set_group_name(self, group_name: str):
        """
        Set the display name for this group.
        
        Args:
            group_name: The new display name for the group
        """
        self.group_name = group_name

    def create_expense(self, expense_id: str, description: str, expense_amount: float,
                                 split_details: List[Split], split_type: ExpenseSplitType, paid_by_user: User) -> Expense:
        """
        Create a new expense within this group.
        
        Creates an expense with the specified details and adds it to the group's
        expense list. The expense is automatically processed by the expense controller
        to update all relevant balance sheets.
        
        Args:
            expense_id: Unique identifier for the expense
            description: Description of the expense
            expense_amount: Total amount of the expense
            split_details: List of Split objects defining how the expense is divided
            split_type: Type of split (EQUAL, UNEQUAL, PERCENTAGE)
            paid_by_user: The user who paid for the expense
            
        Returns:
            Expense: The created expense object
        """
        expense = self.expense_controller.create_expense(expense_id, description, expense_amount, split_details, split_type, paid_by_user)
        self.expense_list.append(expense)
        return expense
