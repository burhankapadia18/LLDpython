from enums.city import City
from theatre import Theatre
from show import Show
from movie import Movie
from typing import List, Dict

class TheatreController:
    """
    Controller class for managing theatres in the booking system.
    
    This class provides centralized management of theatres including:
    - Adding theatres to cities
    - Retrieving shows for specific movies in cities
    - Maintaining city-wise theatre mappings
    
    The controller maintains two data structures:
    - _city_vs_theatre: Maps cities to lists of theatres in that city
    - _all_theatre: Complete list of all theatres in the system
    
    Attributes:
        _city_vs_theatre (Dict[City, List[Theatre]]): Mapping of cities to their theatres
        _all_theatre (List[Theatre]): Complete list of all theatres in the system
    """

    _city_vs_theatre: Dict[City, List[Theatre]]
    _all_theatre: List[Theatre]

    def __init__(self):
        """
        Initialize the TheatreController.
        
        Creates empty data structures for storing theatres and city-theatre mappings.
        """
        self._city_vs_theatre = {}
        self._all_theatre = []


    def add_theatre(self, theatre: Theatre, city: City):
        """
        Add a theatre to a specific city.
        
        This method adds the theatre to both the complete theatre list and
        the city-specific theatre list. If the city doesn't exist in the
        mapping, it creates a new entry.
        
        Args:
            theatre (Theatre): The theatre to add
            city (City): The city where the theatre is located
        """
        self._all_theatre.append(theatre)

        theatres = self._city_vs_theatre.get(city, [])
        theatres.append(theatre)
        self._city_vs_theatre[city] = theatres



    def get_all_show(self, movie: Movie, city: City):
        """
        Get all shows for a specific movie in a specific city.
        
        This method searches through all theatres in the specified city
        and finds all shows for the given movie. It returns a mapping
        of theatres to their shows for that movie.
        
        Args:
            movie (Movie): The movie to find shows for
            city (City): The city to search in
            
        Returns:
            Dict[Theatre, List[Show]]: Mapping of theatres to their shows
                                      for the specified movie, empty dict if no shows found
        """
        theatre_vs_shows = {}
        theatres = self._city_vs_theatre.get(city, [])

        for theatre in theatres:
            given_movie_shows = []
            shows = theatre.get_shows()

            for show in shows:
                if show.get_movie().get_movie_id() == movie.get_movie_id():
                    given_movie_shows.append(show)

            if given_movie_shows:
                theatre_vs_shows[theatre] = given_movie_shows

        return theatre_vs_shows

