from movie import Movie
from screen import Screen
from typing import List

class Show:
    """
    Represents a movie show in a theatre.
    
    This class encapsulates information about a show including the movie being
    shown, the screen where it's displayed, the start time, and the list of
    booked seats. A show represents a specific screening of a movie at a
    particular time on a specific screen.
    
    Attributes:
        _show_id (int): Unique identifier for the show
        _movie (Movie): The movie being shown
        _screen (Screen): The screen where the show is displayed
        _show_start_time (int): Start time in 24-hour format (e.g., 8 for 8 AM, 16 for 4 PM)
        _booked_seat_ids (List[int]): List of seat IDs that are already booked
    """

    _show_id: int
    _movie: Movie
    _screen: Screen
    _show_start_time: int
    _booked_seat_ids: List[int] = []

    def get_show_id(self):
        """
        Get the unique identifier of the show.
        
        Returns:
            int: The show ID
        """
        return self._show_id

    def set_show_id(self, show_id: int):
        """
        Set the unique identifier for the show.
        
        Args:
            show_id (int): The unique identifier to assign to the show
        """
        self._show_id = show_id


    def get_movie(self):
        """
        Get the movie being shown in this show.
        
        Returns:
            Movie: The movie object
        """
        return self._movie


    def set_movie(self, movie: Movie):
        """
        Set the movie for this show.
        
        Args:
            movie (Movie): The movie to assign to the show
        """
        self._movie = movie

    def get_screen(self):
        """
        Get the screen where this show is displayed.
        
        Returns:
            Screen: The screen object
        """
        return self._screen

    def set_screen(self, screen: Screen):
        """
        Set the screen for this show.
        
        Args:
            screen (Screen): The screen to assign to the show
        """
        self._screen = screen

    def get_show_start_time(self):
        """
        Get the start time of the show.
        
        Returns:
            int: The start time in 24-hour format (e.g., 8 for 8 AM, 16 for 4 PM)
        """
        return self._show_start_time

    def set_show_start_time(self, show_start_time: int):
        """
        Set the start time for the show.
        
        Args:
            show_start_time (int): The start time in 24-hour format
        """
        self._show_start_time = show_start_time

    def get_booked_seat_ids(self):
        """
        Get the list of seat IDs that are already booked for this show.
        
        Returns:
            List[int]: List of booked seat IDs
        """
        return self._booked_seat_ids

    def set_booked_seat_ids(self, booked_seat_ids: List[int]):
        """
        Set the list of booked seat IDs for this show.
        
        Args:
            booked_seat_ids (List[int]): List of seat IDs that are booked
        """
        self._booked_seat_ids = booked_seat_ids
