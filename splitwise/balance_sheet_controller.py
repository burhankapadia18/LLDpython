"""
Balance Sheet Controller Module

This module manages the balance sheet calculations and updates for users in the Splitwise system.
It handles the complex logic of tracking who owes what to whom and updating balance sheets
when expenses are created or modified.

The BalanceSheetController class provides functionality to:
- Update user expense balance sheets when expenses are created
- Calculate and track amounts owed and amounts to be received
- Display balance sheets for individual users
- Manage the relationship between expense payers and beneficiaries
"""

from expense.split.split import Split
from user.user import User
from balance import Balance
from typing import List

class BalanceSheetController:
    """
    Controller class for managing user balance sheets in the Splitwise system.
    
    This class handles all balance sheet related operations including:
    - Updating balance sheets when expenses are created
    - Calculating amounts owed and amounts to be received
    - Managing the balance relationships between users
    - Displaying formatted balance sheet information
    """

    def update_user_expense_balance_sheet(self, expense_paid_by: User, splits: List[Split], total_expense_amount: float):
        """
        Update the balance sheets for all users involved in an expense.
        
        This method performs the core balance sheet update logic:
        1. Updates the payer's total payment amount
        2. For each split, updates the balance between payer and beneficiary
        3. Handles special cases where the payer is also a beneficiary
        4. Maintains the balance relationships between all users
        
        Args:
            expense_paid_by: The user who paid for the expense
            splits: List of Split objects representing how the expense is divided
            total_expense_amount: The total amount of the expense
        """
        # Update the total amount paid of the expense paid by user
        paid_by_user_expense_sheet = expense_paid_by.get_user_expense_balance_sheet()
        paid_by_user_expense_sheet.set_total_payment(paid_by_user_expense_sheet.get_total_payment() + total_expense_amount)

        for split in splits:
            user_owe = split.get_user()
            owe_user_expense_sheet = user_owe.get_user_expense_balance_sheet()
            owe_amount = split.get_amount_owe()

            if expense_paid_by.get_user_id() == user_owe.get_user_id():
                # If the payer is also a beneficiary, update their own expense
                paid_by_user_expense_sheet.set_total_your_expense(paid_by_user_expense_sheet.get_total_your_expense()+owe_amount)
            else:
                # Update the balance of paid user (amount they should receive)
                paid_by_user_expense_sheet.set_total_you_get_back(paid_by_user_expense_sheet.get_total_you_get_back() + owe_amount)

                # Get or create balance object for the relationship between payer and beneficiary
                if user_owe.get_user_id() in paid_by_user_expense_sheet.get_user_vs_balance():
                    user_owe_balance = paid_by_user_expense_sheet.get_user_vs_balance().get(user_owe.get_user_id())
                else:
                    user_owe_balance = Balance()
                    paid_by_user_expense_sheet.get_user_vs_balance()[user_owe.get_user_id()] = user_owe_balance

                # Update the amount the payer should get back from this beneficiary
                user_owe_balance.set_amount_get_back(user_owe_balance.get_amount_get_back() + owe_amount)

                # Update the balance sheet of the beneficiary (amount they owe)
                owe_user_expense_sheet.set_total_you_owe(owe_user_expense_sheet.get_total_you_owe() + owe_amount)
                owe_user_expense_sheet.set_total_your_expense(owe_user_expense_sheet.get_total_your_expense() + owe_amount)

                # Get or create balance object for the relationship between beneficiary and payer
                user_paid_balance = None
                if expense_paid_by.get_user_id() in owe_user_expense_sheet.get_user_vs_balance():
                    user_paid_balance = owe_user_expense_sheet.get_user_vs_balance().get(expense_paid_by.get_user_id())
                else:
                    user_paid_balance = Balance()
                    owe_user_expense_sheet.get_user_vs_balance()[expense_paid_by.get_user_id()] = user_paid_balance
                
                # Update the amount the beneficiary owes to the payer
                user_paid_balance.set_amount_owe(user_paid_balance.get_amount_owe() + owe_amount)

    def show_balance_sheet_of_user(self, user: User):
        """
        Display the complete balance sheet for a specific user.
        
        This method prints a formatted balance sheet showing:
        - Total expenses incurred by the user
        - Total amount the user should receive from others
        - Total amount the user owes to others
        - Total payments made by the user
        - Detailed breakdown of balances with each other user
        
        Args:
            user: The user whose balance sheet should be displayed
        """
        print("---------------------------------------")
        print("Balance sheet of user : " + user.get_user_id())

        user_expense_balance_sheet =  user.get_user_expense_balance_sheet()
        print("TotalYourExpense: " + str(user_expense_balance_sheet.get_total_your_expense()))
        print("TotalGetBack: " + str(user_expense_balance_sheet.get_total_you_get_back()))
        print("TotalYourOwe: " + str(user_expense_balance_sheet.get_total_you_owe()))
        print("TotalPaymnetMade: " + str(user_expense_balance_sheet.get_total_payment()))
        
        # Display detailed balance with each user
        for user_id, balance in user_expense_balance_sheet.get_user_vs_balance().items():
            print("userID:" + user_id + " YouGetBack:" + str(balance.get_amount_get_back()) + " YouOwe:" + str(balance.get_amount_owe()))
        print("---------------------------------------")
        print("---------------------------------------")
