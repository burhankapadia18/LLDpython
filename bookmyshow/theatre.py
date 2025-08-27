from enums.city import City
from screen import Screen
from show import Show
from typing import List

class Theatre:
    """
    Represents a movie theatre in the booking system.
    
    This class encapsulates all the essential information about a theatre including
    its location, screens, and shows. A theatre can have multiple screens, and
    each screen can host multiple shows for different movies.
    
    Attributes:
        _theatre_id (int): Unique identifier for the theatre
        _address (str): Physical address of the theatre
        _city (City): City where the theatre is located
        _screens (List[Screen]): List of screens in the theatre
        _shows (List[Show]): List of shows running in the theatre
    """

    _theatre_id: int
    _address: str
    _city: City
    _screens: List[Screen]
    _shows: List[Show]

    def get_theatre_id(self):
        """
        Get the unique identifier of the theatre.
        
        Returns:
            int: The theatre ID
        """
        return self._theatre_id

    def set_theatre_id(self, theatre_id: int):
        """
        Set the unique identifier for the theatre.
        
        Args:
            theatre_id (int): The unique identifier to assign to the theatre
        """
        self._theatre_id = theatre_id


    def get_address(self):
        """
        Get the physical address of the theatre.
        
        Returns:
            str: The theatre address
        """
        return self._address


    def set_address(self, address: str):
        """
        Set the physical address of the theatre.
        
        Args:
            address (str): The address to assign to the theatre
        """
        self._address = address

    def get_screens(self):
        """
        Get all screens in the theatre.
        
        Returns:
            List[Screen]: List of all screens in the theatre
        """
        return self._screens

    def set_screens(self, screens: List[Screen]):
        """
        Set the screens for the theatre.
        
        Args:
            screens (List[Screen]): List of screens to assign to the theatre
        """
        self._screens = screens

    def get_shows(self):
        """
        Get all shows running in the theatre.
        
        Returns:
            List[Show]: List of all shows in the theatre
        """
        return self._shows

    def set_shows(self, shows: List[Show]):
        """
        Set the shows for the theatre.
        
        Args:
            shows (List[Show]): List of shows to assign to the theatre
        """
        self._shows = shows

    def get_city(self):
        """
        Get the city where the theatre is located.
        
        Returns:
            City: The city enum value
        """
        return self._city

    def set_city(self, city: City):
        """
        Set the city where the theatre is located.
        
        Args:
            city (City): The city enum value to assign to the theatre
        """
        self._city = city
