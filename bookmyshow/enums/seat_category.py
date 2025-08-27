from enum import Enum

class SeatCategory(Enum):
    """
    Enumeration of seat categories in a movie screen.
    
    This enum defines the different categories of seats available in a screen.
    Each category typically has different pricing and location within the screen.
    
    Values:
        SILVER: Basic category seats, usually located in the front rows
        GOLD: Premium category seats, usually located in the middle rows
        PLATINUM: Luxury category seats, usually located in the back rows
    """
    SILVER = "SILVER"
    GOLD = "GOLD"
    PLATINUM = "PLATINUM"
