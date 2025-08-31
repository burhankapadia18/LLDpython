"""
User Controller Module

This module defines the UserController class which manages all user-related operations
in the Splitwise system. It provides functionality to add, retrieve, and manage users.

The UserController serves as the central point for user management, maintaining
a list of all users in the system and providing methods to interact with them.
"""

from user.user import User
from typing import List

class UserController:
    """
    Controller class for managing users in the Splitwise system.
    
    This class maintains a list of all users in the system and provides
    methods to add new users, retrieve existing users, and get all users.
    
    Attributes:
        user_list: List of all users in the system
    """

    user_list: List[User]

    def __init__(self):
        """
        Initialize the UserController with an empty user list.
        
        Creates a new UserController instance with an empty list to store users.
        """
        self.user_list = []

    def add_user(self, user: User):
        """
        Add a new user to the system.
        
        Adds the specified user to the list of users managed by this controller.
        
        Args:
            user: The User object to add to the system
        """
        self.user_list.append(user)

    def get_user(self, user_id: str) -> User:
        """
        Retrieve a user by their unique identifier.
        
        Searches through the list of users to find one with the matching user ID.
        
        Args:
            user_id: The unique identifier of the user to find
            
        Returns:
            User: The user with the matching ID, or None if not found
        """
        for user in self.user_list:
            if (user.get_user_id() == user_id):
                return user 
        return None

    def get_all_users(self) -> List[User]:
        """
        Get all users in the system.
        
        Returns:
            List[User]: List of all users managed by this controller
        """
        return self.user_list
