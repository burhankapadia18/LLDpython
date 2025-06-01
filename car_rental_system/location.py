"""
Location Management Module

This module provides location representation and management functionality
for the car rental system. It defines the Location class which stores
geographical information used throughout the system for store locations,
pickup/drop-off points, and user addresses.

Classes:
    Location: Represents a geographical location with address components
"""


class Location:
    """
    Represents a geographical location within the rental system.
    
    The Location class stores address information including pincode, city,
    state, and country. This class is used throughout the system to represent
    store locations, pickup/drop-off points, and user addresses.
    
    Attributes:
        address (str): Full street address (currently unused)
        pincode (int): Postal/ZIP code for the location
        city (str): City name
        state (str): State or province name
        country (str): Country name
    """
    
    address: str
    pincode: int
    city: str
    state: str
    country: str

    def __init__(self, pincode: int, city: str, state: str, country: str):
        """
        Initialize a new location with the provided address components.
        
        Args:
            pincode (int): Postal/ZIP code for the location
            city (str): City name
            state (str): State or province name
            country (str): Country name
        """
        self.pincode = pincode
        self.city = city
        self.state = state
        self.country = country
