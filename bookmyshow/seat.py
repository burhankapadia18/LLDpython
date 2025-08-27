from enums.seat_category import SeatCategory

class Seat:
    """
    Represents a seat in a movie screen.
    
    This class encapsulates information about a seat including its unique
    identifier, row number, and category (Silver, Gold, Platinum). The seat
    category determines the pricing and location within the screen.
    
    Attributes:
        _seat_id (int): Unique identifier for the seat
        _row (int): Row number where the seat is located
        _seat_category (SeatCategory): Category of the seat (SILVER, GOLD, PLATINUM)
    """
    _seat_id: int
    _row: int
    _seat_category: SeatCategory

    def get_seat_id(self):
        """
        Get the unique identifier of the seat.
        
        Returns:
            int: The seat ID
        """
        return self._seat_id

    def set_seat_id(self, seat_id: int):
        """
        Set the unique identifier for the seat.
        
        Args:
            seat_id (int): The unique identifier to assign to the seat
        """
        self._seat_id = seat_id

    def get_row(self):
        """
        Get the row number where the seat is located.
        
        Returns:
            int: The row number
        """
        return self._row

    def set_row(self, row: int):
        """
        Set the row number for the seat.
        
        Args:
            row (int): The row number to assign to the seat
        """
        self._row = row

    def get_seat_category(self):
        """
        Get the category of the seat.
        
        Returns:
            SeatCategory: The seat category (SILVER, GOLD, or PLATINUM)
        """
        return self._seat_category

    def set_seat_category(self, seat_category: SeatCategory):
        """
        Set the category for the seat.
        
        Args:
            seat_category (SeatCategory): The seat category to assign (SILVER, GOLD, or PLATINUM)
        """
        self._seat_category = seat_category
