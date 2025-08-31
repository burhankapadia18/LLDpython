"""
Splitwise Application - Main Controller

This module serves as the main controller for the Splitwise expense splitting application.
It orchestrates user management, group management, and expense tracking functionality.

The Splitwise class provides a high-level interface for:
- Managing users and their expense balance sheets
- Creating and managing groups
- Handling expense creation and balance sheet updates
- Demonstrating the application functionality
"""

from expense.expense_split_type import ExpenseSplitType
from expense.split.split import Split
from group.group_controller import GroupController
from user.user import User
from user.user_controller import UserController
from balance_sheet_controller import BalanceSheetController


class Splitwise:
    """
    Main controller class for the Splitwise expense splitting application.
    
    This class coordinates between different controllers to provide a unified
    interface for managing users, groups, and expenses in the Splitwise system.
    
    Attributes:
        user_controller: Controller for managing users
        group_controller: Controller for managing groups
        balance_sheet_controller: Controller for managing balance sheets
    """

    user_controller: UserController
    group_controller: GroupController
    balance_sheet_controller: BalanceSheetController

    def __init__(self):
        """
        Initialize the Splitwise application with all necessary controllers.
        
        Creates instances of UserController, GroupController, and BalanceSheetController
        to manage different aspects of the application.
        """
        self.user_controller = UserController()
        self.group_controller = GroupController()
        self.balance_sheet_controller = BalanceSheetController()

    def demo(self):
        """
        Demonstrate the Splitwise application functionality.
        
        This method showcases the complete workflow of the application:
        1. Sets up users and groups
        2. Adds members to groups
        3. Creates expenses with different split types
        4. Displays balance sheets for all users
        
        The demo creates sample data to show how the system handles
        equal and unequal expense splitting scenarios.
        """
        # Setup initial users and groups
        self.setup_user_and_group()

        # Step 1: Add members to the group
        group = self.group_controller.get_group("G1001")
        group.add_member(self.user_controller.get_user("U2001"))
        group.add_member(self.user_controller.get_user("U3001"))

        # Step 2: Create an expense inside a group with EQUAL split
        splits = []
        split1 = Split(self.user_controller.get_user("U1001"), 300)
        split2 = Split(self.user_controller.get_user("U2001"), 300)
        split3 = Split(self.user_controller.get_user("U3001"), 300)
        splits.append(split1)
        splits.append(split2)
        splits.append(split3)
        group.create_expense("Exp1001", "Breakfast", 900, splits, ExpenseSplitType.EQUAL, self.user_controller.get_user("U1001"))

        # Step 3: Create another expense with UNEQUAL split
        splits2 = []
        splits2_1 = Split(self.user_controller.get_user("U1001"), 400)
        splits2_2 = Split(self.user_controller.get_user("U2001"), 100)
        splits2.append(splits2_1)
        splits2.append(splits2_2)
        group.create_expense("Exp1002", "Lunch", 500, splits2, ExpenseSplitType.UNEQUAL, self.user_controller.get_user("U2001"))

        # Display balance sheets for all users
        for user in self.user_controller.get_all_users():
            self.balance_sheet_controller.show_balance_sheet_of_user(user)

    def setup_user_and_group(self):
        """
        Set up initial users and create a group for demonstration.
        
        This method:
        1. Adds users to the Splitwise application
        2. Creates a new group with the first user as the creator
        """
        # Onboard users to splitwise app
        self.add_users_to_splitwise_app()
        # Create a group by user1
        user1 = self.user_controller.get_user("U1001")
        self.group_controller.create_new_group("G1001", "Outing with Friends", user1)

    def add_users_to_splitwise_app(self):
        """
        Add sample users to the Splitwise application.
        
        Creates three users with unique IDs and names for demonstration purposes.
        Each user is added to the user controller for management.
        """
        # Adding User1
        user1 = User("U1001", "User1")
        # Adding User2
        user2 = User("U2001", "User2")
        # Adding User3
        user3 = User("U3001", "User3")
        self.user_controller.add_user(user1)
        self.user_controller.add_user(user2)
        self.user_controller.add_user(user3)
