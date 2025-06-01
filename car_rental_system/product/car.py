"""
Car Vehicle Implementation

This module provides the Car class, which is a concrete implementation of
the Vehicle abstract base class. It represents four-wheeled passenger
vehicles available for rental in the system.

Classes:
    Car: Concrete implementation for car vehicles
"""

from .vehicle import Vehicle, VehicleType

class Car(Vehicle):
    """
    Concrete implementation of Vehicle for car-type vehicles.
    
    The Car class represents four-wheeled passenger vehicles in the rental
    system. It inherits all functionality from the Vehicle base class and
    automatically sets the vehicle type to CAR during initialization.
    
    This class can be extended to include car-specific functionality such as:
    - Number of doors
    - Transmission type (manual/automatic)
    - Fuel type (petrol/diesel/electric)
    - Air conditioning availability
    """

    def __init__(self, **kwargs):
        """
        Initialize a new Car instance.
        
        Creates a new car vehicle and automatically sets the vehicle type
        to CAR. All other vehicle attributes are inherited from the base
        Vehicle class.
        
        Args:
            **kwargs: Keyword arguments passed to the parent Vehicle class
        """
        super().__init__(**kwargs)
        self.set_vehicle_type(VehicleType.CAR)