"""
Billing Module

This module handles billing and payment calculation functionality for the car rental system.
It provides the Bill class which calculates rental costs based on reservations and tracks
payment status.

The Bill class integrates with the reservation system to compute appropriate charges
and maintains the payment state throughout the rental process.

Classes:
    Bill: Handles billing calculations and payment tracking
"""

from reservation import Reservation


class Bill:
    """
    Represents a billing record for a vehicle rental reservation.
    
    The Bill class is responsible for calculating the total rental cost
    based on the reservation details and tracking whether the bill has
    been paid. It serves as the primary interface between reservations
    and the payment system.
    
    Attributes:
        reservation (Reservation): The reservation this bill is associated with
        totalBillAmount (float): The calculated total amount due for the rental
        isBillPaid (bool): Flag indicating whether the bill has been paid
    """

    reservation: Reservation
    totalBillAmount: float
    isBillPaid: bool

    def __init__(self, reservation: Reservation):
        """
        Initialize a new bill for the given reservation.
        
        Creates a new billing record, calculates the total amount due,
        and sets the initial payment status to unpaid.
        
        Args:
            reservation (Reservation): The reservation to generate a bill for
        """
        self.reservation = reservation
        self.totalBillAmount = self.compute_bill_amount()
        self.isBillPaid = False

    def compute_bill_amount(self) -> float:
        """
        Calculate the total billing amount for the reservation.
        
        This method computes the rental cost based on the reservation details
        such as rental duration, vehicle type, and applicable rates.
        
        Returns:
            float: The calculated total amount due for the rental
            
        Note:
            Current implementation returns a fixed amount of 100.0.
            In a production system, this would calculate based on:
            - Rental duration (daily/hourly rates)
            - Vehicle type and pricing tier
            - Additional fees and taxes
            - Discounts and promotions
        """

        return 100.0
