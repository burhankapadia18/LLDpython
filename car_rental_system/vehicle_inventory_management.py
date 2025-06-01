"""
Vehicle Inventory Management Module

This module provides inventory management functionality for vehicle rental stores.
It handles the storage, retrieval, and management of vehicle collections within
individual store locations.

The VehicleInventoryManagement class serves as the interface between stores
and their vehicle inventories, providing methods for filtering and managing
available vehicles.

Classes:
    VehicleInventoryManagement: Manages vehicle inventory for stores
"""

from product.vehicle import Vehicle
from typing import List

#vehicle inventory management
class VehicleInventoryManagement:
    """
    Manages vehicle inventory for rental stores.
    
    This class provides inventory management capabilities for individual
    stores within the rental system. It handles the storage and retrieval
    of vehicles, and can be extended to provide filtering, searching,
    and availability checking functionality.
    
    Attributes:
        vehicles (List[Vehicle]): List of vehicles in the inventory
    """

    vehicles: List[Vehicle]

    #constructor
    def __init__(self, vehicles: List[Vehicle]):
        """
        Initialize the inventory management system with a list of vehicles.
        
        Args:
            vehicles (List[Vehicle]): Initial list of vehicles to manage
        """
        self.vehicles = vehicles

    def get_vehicles(self) -> List[Vehicle]:
        """
        Retrieve all vehicles in the inventory.
        
        This method returns the complete list of vehicles currently
        managed by this inventory system. In a production system,
        this method could be extended to support filtering by:
        - Vehicle type (car, bike, etc.)
        - Availability status
        - Price range
        - Vehicle features
        
        Returns:
            List[Vehicle]: List of all vehicles in the inventory
        """
        #filtering
        return self.vehicles

    #setter
    def set_vehicles(self, vehicles: List[Vehicle]) -> None:
        """
        Update the inventory with a new list of vehicles.
        
        This method replaces the current vehicle inventory with
        the provided list of vehicles.
        
        Args:
            vehicles (List[Vehicle]): New list of vehicles to manage
        """
        self.vehicles = vehicles
