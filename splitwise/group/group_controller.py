"""
Group Controller Module

This module defines the GroupController class which manages all group-related operations
in the Splitwise system. It provides functionality to create, retrieve, and manage groups.

The GroupController serves as the central point for group management, maintaining
a list of all groups in the system and providing methods to interact with them.
"""

from group.group import Group
from user.user import User
from typing import List


class GroupController:
    """
    Controller class for managing groups in the Splitwise system.
    
    This class maintains a list of all groups in the system and provides
    methods to create new groups, retrieve existing groups, and manage group operations.
    
    Attributes:
        group_list: List of all groups in the system
    """

    group_list: List[Group]

    def __init__(self):
        """
        Initialize the GroupController with an empty group list.
        
        Creates a new GroupController instance with an empty list to store groups.
        """
        self.group_list = []

    def create_new_group(self, group_id: str, group_name: str, created_by_user: User):
        """
        Create a new group in the system.
        
        Creates a new group with the specified ID and name, adds the creator
        as the first member, and adds the group to the list of managed groups.
        
        Args:
            group_id: Unique identifier for the new group
            group_name: Display name for the new group
            created_by_user: The user who is creating the group (becomes first member)
        """
        # Create a new group
        group = Group()
        group.set_group_id(group_id)
        group.set_group_name(group_name)
        # Add the user into the group, as it is created by the USER
        group.add_member(created_by_user)
        # Add the group in the list of overall groups
        self.group_list.append(group)

    def get_group(self, group_id: str) -> Group:
        """
        Retrieve a group by its unique identifier.
        
        Searches through the list of groups to find one with the matching group ID.
        
        Args:
            group_id: The unique identifier of the group to find
            
        Returns:
            Group: The group with the matching ID, or None if not found
        """
        for group in self.group_list:
            if group.get_group_id() == group_id:
                return group
        return None
