"""
User Management Module

This module provides user representation and management functionality for
the car rental system. It defines the User class which stores customer
information including personal details and driving credentials.

Classes:
    User: Represents a customer in the rental system
"""


class User:
    """
    Represents a customer/user in the vehicle rental system.
    
    The User class stores essential customer information including
    identification, personal details, and driving credentials required
    for vehicle rental transactions.
    
    Attributes:
        userId (int): Unique identifier for the user
        userName (int): User's name (Note: type should be str in production)
        drivingLicense (int): Driving license number/ID
    
    Note:
        The userName field is currently typed as int but should be str
        in a production system. This appears to be a design oversight.
    """

    userId: int
    userName: int
    drivingLicense: int

    def get_user_id(self) -> int:
        """
        Get the user's unique identifier.
        
        Returns:
            int: The user's unique identifier
        """
        return self.userId

    def set_user_id(self, userId: int) -> None:
        """
        Set the user's unique identifier.
        
        Args:
            userId (int): Unique identifier for this user
        """
        self.userId = userId

    def get_user_name(self) -> int:
        """
        Get the user's name.
        
        Returns:
            int: The user's name
            
        Note:
            Return type should be str in a production system.
        """
        return self.userName

    def set_user_name(self, userName: int) -> None:
        """
        Set the user's name.
        
        Args:
            userName (int): The user's name
            
        Note:
            Parameter type should be str in a production system.
        """
        self.userName = userName

    def get_driving_license(self) -> int:
        """
        Get the user's driving license number.
        
        Returns:
            int: The user's driving license number/ID
        """
        return self.drivingLicense

    def set_driving_license(self, drivingLicense: int) -> None:
        """
        Set the user's driving license number.
        
        Args:
            drivingLicense (int): The user's driving license number/ID
        """
        self.drivingLicense = drivingLicense
