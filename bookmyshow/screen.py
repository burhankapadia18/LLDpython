from seat import Seat
from typing import List

class Screen:
    """
    Represents a movie screen in a theatre.
    
    This class encapsulates information about a screen including its unique
    identifier and the seats available on that screen. Each screen can have
    multiple seats of different categories (Silver, Gold, Platinum).
    
    Attributes:
        _screen_id (int): Unique identifier for the screen
        _seats (List[Seat]): List of seats available on this screen
    """

    _screen_id: int
    _seats: List[Seat]

    def get_screen_id(self):
        """
        Get the unique identifier of the screen.
        
        Returns:
            int: The screen ID
        """
        return self._screen_id

    def set_screen_id(self, screen_id: int):
        """
        Set the unique identifier for the screen.
        
        Args:
            screen_id (int): The unique identifier to assign to the screen
        """
        self._screen_id = screen_id

    def get_seats(self):
        """
        Get all seats on this screen.
        
        Returns:
            List[Seat]: List of all seats on the screen
        """
        return self._seats

    def set_seats(self, seats: List[Seat]):
        """
        Set the seats for this screen.
        
        Args:
            seats (List[Seat]): List of seats to assign to the screen
        """
        self._seats = seats
