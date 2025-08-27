from movie import Movie
from enums.city import City
from typing import List, Dict

class MovieController:
    """
    Controller class for managing movies in the booking system.
    
    This class provides centralized management of movies including:
    - Adding movies to cities
    - Retrieving movies by city, name, or ID
    - Removing and updating movies
    - Maintaining city-wise movie mappings
    
    The controller maintains two data structures:
    - _city_vs_movies: Maps cities to lists of movies available in that city
    - _all_movies: Complete list of all movies in the system
    
    Attributes:
        _city_vs_movies (Dict[City, List[Movie]]): Mapping of cities to their available movies
        _all_movies (List[Movie]): Complete list of all movies in the system
    """

    _city_vs_movies: Dict[City, List[Movie]]
    _all_movies: List[Movie]

    def __init__(self):
        """
        Initialize the MovieController.
        
        Creates empty data structures for storing movies and city-movie mappings.
        """
        self._city_vs_movies = {}
        self._all_movies = []


    def add_movie(self, movie: Movie, city: City):
        """
        Add a movie to a specific city.
        
        This method adds the movie to both the complete movie list and
        the city-specific movie list. If the city doesn't exist in the
        mapping, it creates a new entry.
        
        Args:
            movie (Movie): The movie to add
            city (City): The city where the movie should be available
        """
        self._all_movies.append(movie)

        movies = self._city_vs_movies.get(city, [])
        movies.append(movie)
        self._city_vs_movies[city] = movies



    def get_movie_by_name(self, movie_name: str):
        """
        Get a movie by its name.
        
        Searches through all movies in the system to find a movie with
        the specified name.
        
        Args:
            movie_name (str): The name of the movie to find
            
        Returns:
            Movie: The movie object if found, None otherwise
        """
        for movie in self._all_movies:
            if movie.get_movie_name() == movie_name:
                return movie
        return None



    def get_movies_by_city(self, city: City):
        """
        Get all movies available in a specific city.
        
        Args:
            city (City): The city to get movies for
            
        Returns:
            List[Movie]: List of movies available in the specified city,
                        or None if no movies are found for that city
        """
        return self._city_vs_movies.get(city)

    def remove_movie_from_city(self, movie: Movie, city: City):
        """
        Remove a movie from a specific city.
        
        Removes the movie from the city's movie list but keeps it in
        the overall movie list.
        
        Args:
            movie (Movie): The movie to remove
            city (City): The city from which to remove the movie
        """
        self._city_vs_movies[city].remove(movie)

    def update_movie_in_city(self, movie: Movie, city: City):
        """
        Update a movie in a specific city.
        
        This method removes the existing movie entry and adds the updated
        movie back to the city's movie list.
        
        Args:
            movie (Movie): The updated movie object
            city (City): The city where the movie should be updated
        """
        self._city_vs_movies[city].remove(movie)
        self._city_vs_movies[city].append(movie)

    def get_movie_by_id(self, movie_id: int):
        """
        Get a movie by its unique identifier.
        
        Searches through all movies in the system to find a movie with
        the specified ID.
        
        Args:
            movie_id (int): The unique identifier of the movie to find
            
        Returns:
            Movie: The movie object if found, None otherwise
        """
        for movie in self._all_movies:
            if movie.get_movie_id() == movie_id:
                return movie
