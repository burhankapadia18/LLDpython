from enum import Enum

class City(Enum):
    """
    Enumeration of cities where theatres are located.
    
    This enum defines the cities that are supported in the booking system.
    Each city can have multiple theatres and movies available.
    
    Values:
        Bangalore: Bangalore city
        Delhi: Delhi city
    """
    Bangalore = "Bangalore"
    Delhi = "Delhi"
