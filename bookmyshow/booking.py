from show import Show
from seat import Seat
from payment import Payment
from typing import List

class Booking:
    """
    Represents a movie booking made by a user.
    
    This class encapsulates all the information related to a booking including
    the show being booked, the seats selected, and the payment information.
    A booking represents a confirmed reservation for a specific show with
    selected seats.
    
    Attributes:
        _show (Show): The show for which the booking is made
        _booked_seats (List[Seat]): List of seats booked in this booking
        _payment (Payment): Payment information for this booking
    """

    _show: Show
    _booked_seats: List[Seat]
    _payment: Payment

    def get_show(self):
        """
        Get the show for which this booking is made.
        
        Returns:
            Show: The show object
        """
        return self._show

    def set_show(self, show: Show):
        """
        Set the show for this booking.
        
        Args:
            show (Show): The show to assign to the booking
        """
        self._show = show

    def get_booked_seats(self):
        """
        Get the list of seats booked in this booking.
        
        Returns:
            List[Seat]: List of booked seat objects
        """
        return self._booked_seats

    def set_booked_seats(self, booked_seats: List[Seat]):
        """
        Set the list of booked seats for this booking.
        
        Args:
            booked_seats (List[Seat]): List of seat objects to assign to the booking
        """
        self._booked_seats = booked_seats

    def get_payment(self):
        """
        Get the payment information for this booking.
        
        Returns:
            Payment: The payment object
        """
        return self._payment

    def set_payment(self, payment: Payment):
        """
        Set the payment information for this booking.
        
        Args:
            payment (Payment): The payment object to assign to the booking
        """
        self._payment = payment
