"""
Bike Vehicle Implementation

This module provides the Bike class, which is a concrete implementation of
the Vehicle abstract base class. It represents two-wheeled motor vehicles
available for rental in the system.

Classes:
    Bike: Concrete implementation for bike/motorcycle vehicles
"""

from .vehicle import Vehicle, VehicleType

class Bike(Vehicle):
    """
    Concrete implementation of Vehicle for bike/motorcycle-type vehicles.
    
    The Bike class represents two-wheeled motor vehicles in the rental
    system. It inherits all functionality from the Vehicle base class and
    automatically sets the vehicle type to BIKE during initialization.
    
    This class can be extended to include bike-specific functionality such as:
    - Engine type (2-stroke/4-stroke)
    - Gear type (manual/automatic)
    - Storage capacity
    - Safety features (ABS, etc.)
    """

    def __init__(self, **kwargs):
        """
        Initialize a new Bike instance.
        
        Creates a new bike/motorcycle vehicle and automatically sets the
        vehicle type to BIKE. All other vehicle attributes are inherited
        from the base Vehicle class.
        
        Args:
            **kwargs: Keyword arguments passed to the parent Vehicle class
        """
        super().__init__(**kwargs)
        self.set_vehicle_type(VehicleType.BIKE)
