"""
Reservation Management Module

This module handles vehicle reservation functionality within the car rental system.
It defines reservation types, statuses, and the core Reservation class that manages
booking details, dates, locations, and user information.

The module supports different reservation types (daily/hourly) and tracks
reservation status throughout the rental lifecycle.

Classes:
    ReservationType: Enumeration of available reservation types
    ReservationStatus: Enumeration of possible reservation statuses
    Reservation: Core class for managing vehicle reservations
"""

from product.vehicle import Vehicle
from user import User
from location import Location
from datetime import datetime
from enum import Enum
import random


class ReservationType(Enum):
    """
    Enumeration of available reservation types.
    
    Attributes:
        DAILY: Daily rental reservation
        HOURLY: Hourly rental reservation
    """
    DAILY = "Daily"
    HOURLY = "Hourly"

class ReservationStatus(Enum):
    """
    Enumeration of possible reservation statuses.
    
    Attributes:
        SCHEDULED: Reservation is scheduled but not yet started
        COMPLETED: Reservation has been completed successfully
        CANCELLED: Reservation has been cancelled
    """
    SCHEDULED = "Scheduled"
    COMPLETED = "Completed"
    CANCELLED = "Cancelled"

class Reservation:
    """
    Represents a vehicle reservation in the rental system.
    
    This class manages all aspects of a vehicle reservation including user details,
    vehicle information, booking dates, locations, and reservation status. It handles
    the creation and tracking of reservations throughout their lifecycle.
    
    Attributes:
        reservationId (int): Unique identifier for the reservation
        user (User): The user who made the reservation
        vehicle (Vehicle): The vehicle being reserved
        bookingDate (datetime): Date when the reservation was made
        dateBookedFrom (datetime): Start date of the reservation period
        dateBookedTo (datetime): End date of the reservation period
        fromTimeStamp (int): Start timestamp for the reservation
        toTimeStamp (int): End timestamp for the reservation
        pickUpLocation (Location): Location where the vehicle will be picked up
        dropLocation (Location): Location where the vehicle will be returned
        reservationType (ReservationType): Type of reservation (daily/hourly)
        reservationStatus (ReservationStatus): Current status of the reservation
        location (Location): Primary location associated with the reservation
    """

    reservationId: int
    user: User
    vehicle: Vehicle
    bookingDate: datetime
    dateBookedFrom: datetime
    dateBookedTo: datetime
    fromTimeStamp: int
    toTimeStamp: int
    pickUpLocation: Location
    dropLocation: Location
    reservationType: ReservationType
    reservationStatus: ReservationStatus
    location: Location

    def create_reserve(self, user: User, vehicle: Vehicle) -> int:
        """
        Create a new reservation for the specified user and vehicle.
        
        This method initializes a new reservation with a unique ID, assigns
        the user and vehicle, and sets the reservation type and status to
        default values.
        
        Args:
            user (User): The user making the reservation
            vehicle (Vehicle): The vehicle being reserved
            
        Returns:
            int: The unique reservation ID that was generated
            
        Note:
            Currently sets reservation type to DAILY and status to SCHEDULED
            by default. In a production system, these might be parameterizable.
        """
        #generate new id
        self.reservationId = random.randint(10000, 99999);
        self.user=user;
        self.vehicle=vehicle;
        self.reservationType = ReservationType.DAILY;
        self.reservationStatus = ReservationStatus.SCHEDULED;

        return self.reservationId;

    # CRUD operations
