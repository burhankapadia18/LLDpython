"""
Vehicle Management Module

This module defines the core vehicle hierarchy for the car rental system.
It provides the abstract base Vehicle class and supporting enumerations
for vehicle types and status tracking.

The Vehicle class serves as the foundation for all rentable vehicles in
the system, defining common attributes and providing a standardized
interface for vehicle management.

Classes:
    VehicleType: Enumeration of supported vehicle types
    Status: Enumeration of vehicle status states
    Vehicle: Abstract base class for all rental vehicles
"""

from abc import ABC, abstractmethod
from enum import Enum
from datetime import datetime

class VehicleType(Enum):
    """
    Enumeration of supported vehicle types in the rental system.
    
    Attributes:
        CAR: Four-wheeled passenger vehicle
        BIKE: Two-wheeled motor vehicle
    """
    CAR = "Car"
    BIKE = "Bike"

class Status(Enum):
    """
    Enumeration of possible vehicle status states.
    
    Attributes:
        ACTIVE: Vehicle is available for rental
        INACTIVE: Vehicle is not available for rental
    """
    ACTIVE = "Active"
    INACTIVE = "Inactive"


class Vehicle(ABC):
    """
    Abstract base class for all rental vehicles.
    
    This class defines the common interface and attributes for all types
    of vehicles in the rental system. It provides standardized getters
    and setters for vehicle properties and serves as the foundation for
    specific vehicle implementations.
    
    Attributes:
        vehicle_id (int): Unique identifier for the vehicle
        vehicle_number (int): Registration/license plate number
        vehicle_type (VehicleType): Type of vehicle (car, bike, etc.)
        company_name (str): Manufacturer/brand name
        model_name (str): Specific model name
        km_driven (int): Total kilometers driven
        manufacturing_date (datetime): Date of manufacture
        average (int): Fuel efficiency (km per unit)
        cc (int): Engine capacity in cubic centimeters
        daily_rental_cost (int): Cost per day for rental
        hourly_rental_cost (int): Cost per hour for rental
        no_of_seat (int): Number of passenger seats
        status (Status): Current availability status
    """

    vehicle_id: int
    vehicle_number: int
    vehicle_type: VehicleType
    company_name: str
    model_name: str
    km_driven: int
    manufacturing_date: datetime
    average: int
    cc: int
    daily_rental_cost: int
    hourly_rental_cost: int
    no_of_seat: int
    status: Status

    #getters and setters

    def get_vehicle_id(self) -> int:
        """
        Get the vehicle's unique identifier.
        
        Returns:
            int: The vehicle's unique identifier
        """
        return self.vehicle_id
    
    def set_vehicle_id(self, vehicle_id: int) -> None:
        """
        Set the vehicle's unique identifier.
        
        Args:
            vehicle_id (int): Unique identifier for this vehicle
        """
        self.vehicle_id = vehicle_id


    def get_vehicle_number(self) -> int:
        """
        Get the vehicle's registration/license plate number.
        
        Returns:
            int: The vehicle's registration number
        """
        return self.vehicle_number

    def set_vehicle_number(self, vehicle_number: int) -> None:
        """
        Set the vehicle's registration/license plate number.
        
        Args:
            vehicle_number (int): The vehicle's registration number
        """
        self.vehicle_number = vehicle_number


    def get_vehicle_type(self) -> VehicleType:
        """
        Get the vehicle's type classification.
        
        Returns:
            VehicleType: The type of vehicle (CAR, BIKE, etc.)
        """
        return self.vehicle_type

    def set_vehicle_type(self, vehicle_type: VehicleType) -> None:
        """
        Set the vehicle's type classification.
        
        Args:
            vehicle_type (VehicleType): The type of vehicle
        """
        self.vehicle_type = vehicle_type


    def get_company_name(self) -> str:
        """
        Get the vehicle manufacturer's name.
        
        Returns:
            str: The manufacturer/brand name
        """
        return self.company_name

    def set_company_name(self, company_name: str) -> None:
        """
        Set the vehicle manufacturer's name.
        
        Args:
            company_name (str): The manufacturer/brand name
        """
        self.company_name = company_name


    def get_model_name(self) -> str:
        """
        Get the vehicle's model name.
        
        Returns:
            str: The specific model name
        """
        return self.model_name

    def set_model_name(self, model_name: str) -> None:
        """
        Set the vehicle's model name.
        
        Args:
            model_name (str): The specific model name
        """
        self.model_name = model_name


    def get_km_driven(self) -> int:
        """
        Get the total kilometers driven by the vehicle.
        
        Returns:
            int: Total kilometers on the odometer
        """
        return self.km_driven

    def set_km_driven(self, km_driven: int) -> None:
        """
        Set the total kilometers driven by the vehicle.
        
        Args:
            km_driven (int): Total kilometers on the odometer
        """
        self.km_driven = km_driven


    def get_manufacturing_date(self) -> datetime:
        """
        Get the vehicle's manufacturing date.
        
        Returns:
            datetime: Date when the vehicle was manufactured
        """
        return self.manufacturing_date

    def set_manufacturing_date(self, manufacturing_date: datetime) -> None:
        """
        Set the vehicle's manufacturing date.
        
        Args:
            manufacturing_date (datetime): Date when the vehicle was manufactured
        """
        self.manufacturing_date = manufacturing_date


    def get_average(self) -> int:
        """
        Get the vehicle's fuel efficiency.
        
        Returns:
            int: Fuel efficiency in kilometers per unit of fuel
        """
        return self.average

    def set_average(self, average: int) -> None:
        """
        Set the vehicle's fuel efficiency.
        
        Args:
            average (int): Fuel efficiency in kilometers per unit of fuel
        """
        self.average = average


    def get_cc(self) -> int:
        """
        Get the vehicle's engine capacity.
        
        Returns:
            int: Engine capacity in cubic centimeters
        """
        return self.cc

    def set_cc(self, cc: int) -> None:
        """
        Set the vehicle's engine capacity.
        
        Args:
            cc (int): Engine capacity in cubic centimeters
        """
        self.cc = cc


    def get_daily_rental_cost(self) -> int:
        """
        Get the daily rental cost for the vehicle.
        
        Returns:
            int: Cost per day to rent this vehicle
        """
        return self.daily_rental_cost

    def set_daily_rental_cost(self, daily_rental_cost: int) -> None:
        """
        Set the daily rental cost for the vehicle.
        
        Args:
            daily_rental_cost (int): Cost per day to rent this vehicle
        """
        self.daily_rental_cost = daily_rental_cost


    def get_hourly_rental_cost(self) -> int:
        """
        Get the hourly rental cost for the vehicle.
        
        Returns:
            int: Cost per hour to rent this vehicle
        """
        return self.hourly_rental_cost

    def set_hourly_rental_cost(self, hourly_rental_cost: int) -> None:
        """
        Set the hourly rental cost for the vehicle.
        
        Args:
            hourly_rental_cost (int): Cost per hour to rent this vehicle
        """
        self.hourly_rental_cost = hourly_rental_cost

    def get_no_of_seat(self) -> int:
        """
        Get the number of passenger seats in the vehicle.
        
        Returns:
            int: Number of passenger seats
        """
        return self.no_of_seat

    def set_no_of_seat(self, no_of_seat: int) -> None:
        """
        Set the number of passenger seats in the vehicle.
        
        Args:
            no_of_seat (int): Number of passenger seats
        """
        self.no_of_seat = no_of_seat


    def get_status(self) -> Status:
        """
        Get the vehicle's current availability status.
        
        Returns:
            Status: Current status (ACTIVE or INACTIVE)
        """
        return self.status

    def set_status(self, status: Status) -> None:
        """
        Set the vehicle's availability status.
        
        Args:
            status (Status): New status (ACTIVE or INACTIVE)
        """
        self.status = status
