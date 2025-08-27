class Movie:
    """
    Represents a movie in the booking system.
    
    This class encapsulates all the essential information about a movie including
    its unique identifier, name, and duration. Additional movie details like
    genre, language, cast, etc. can be extended in future implementations.
    
    Attributes:
        _movie_id (int): Unique identifier for the movie
        _movie_name (str): Name/title of the movie
        _movie_duration_in_minutes (int): Duration of the movie in minutes
    """

    _movie_id: int
    _movie_name: str
    _movie_duration_in_minutes: int
    #other details like Genere, Language etc.

    def get_movie_id(self):
        """
        Get the unique identifier of the movie.
        
        Returns:
            int: The movie ID
        """
        return self._movie_id

    def set_movie_id(self, movie_id: int):
        """
        Set the unique identifier for the movie.
        
        Args:
            movie_id (int): The unique identifier to assign to the movie
        """
        self._movie_id = movie_id

    def get_movie_name(self):
        """
        Get the name/title of the movie.
        
        Returns:
            str: The movie name
        """
        return self._movie_name

    def set_movie_name(self, movie_name: str):
        """
        Set the name/title of the movie.
        
        Args:
            movie_name (str): The name/title to assign to the movie
        """
        self._movie_name = movie_name

    def get_movie_duration(self):
        """
        Get the duration of the movie in minutes.
        
        Returns:
            int: The movie duration in minutes
        """
        return self._movie_duration_in_minutes

    def set_movie_duration(self, movie_duration: int):
        """
        Set the duration of the movie in minutes.
        
        Args:
            movie_duration (int): The duration in minutes to assign to the movie
        """
        self._movie_duration_in_minutes = movie_duration
