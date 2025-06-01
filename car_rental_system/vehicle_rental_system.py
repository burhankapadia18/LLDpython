"""
Vehicle Rental System - Core System Controller

This module contains the main VehicleRentalSystem class that acts as the central
controller for the entire rental system. It manages stores and users, and provides
the primary interface for rental operations.

The system maintains collections of stores and users, and provides methods for
locating stores based on geographical location and managing the overall system state.

Classes:
    VehicleRentalSystem: Main system controller class
"""

from typing import List
from store import Store
from user import User
from location import Location


class VehicleRentalSystem:
    """
    Main controller class for the vehicle rental system.
    
    This class serves as the central hub for managing stores and users within
    the rental system. It provides functionality to locate stores based on
    geographical location and manages the overall system state.
    
    Attributes:
        storeList (List[Store]): List of all stores in the system
        userList (List[User]): List of all registered users
    """

    storeList: List[Store]
    userList: List[User]

    def __init__(self, stores: List[Store], users: List[User]):
        """
        Initialize the Vehicle Rental System.
        
        Args:
            stores (List[Store]): Initial list of stores to manage
            users (List[User]): Initial list of users in the system
        """
        self.storeList = stores
        self.userList = users


    def get_store(self, location: Location) -> Store:
        """
        Find and return a store based on the provided location.
        
        This method searches through the available stores and returns
        the most appropriate store for the given location. Currently
        returns the first store as a placeholder implementation.
        
        Args:
            location (Location): The location to search for nearby stores
            
        Returns:
            Store: The store closest to or serving the specified location
            
        Note:
            This is a simplified implementation that returns the first store.
            In a production system, this would implement proper geographical
            search and filtering logic.
        """
        #based on location, we will filter out the Store from storeList.
        return self.storeList[0]

    # addUsers

    #remove users

    #add stores

    #remove stores
