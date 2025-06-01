"""
Store Management Module

This module contains the Store class which represents individual rental locations
within the vehicle rental system. Each store manages its own inventory of vehicles,
handles reservations, and coordinates with the inventory management system.

The Store class provides functionality for:
- Managing vehicle inventory through VehicleInventoryManagement
- Creating and completing reservations
- Filtering available vehicles by type
- Tracking store location and ID

Classes:
    Store: Represents a rental store location
"""

from product.vehicle import Vehicle, VehicleType
from vehicle_inventory_management import VehicleInventoryManagement
from typing import List
from location import Location
from reservation import Reservation
from user import User


class Store:
    """
    Represents a vehicle rental store location.
    
    The Store class manages vehicle inventory, handles customer reservations,
    and coordinates rental operations at a specific location. Each store
    maintains its own inventory through the VehicleInventoryManagement system
    and tracks active reservations.
    
    Attributes:
        storeId (int): Unique identifier for the store
        inventoryManagement (VehicleInventoryManagement): Manages vehicle inventory
        storeLocation (Location): Physical location of the store
        reservations (List[Reservation]): List of active reservations
    """

    storeId: int
    inventoryManagement: VehicleInventoryManagement
    storeLocation: Location
    reservations: List[Reservation] = []


    def set_store_id(self, storeId: int) -> None:
        """
        Set the store's unique identifier.
        
        Args:
            storeId (int): Unique identifier for this store
        """
        self.storeId = storeId

    def get_store_id(self) -> int:
        """
        Get the store's unique identifier.
        
        Returns:
            int: The store's unique identifier
        """
        return self.storeId


    def get_vehicles(self, vehicleType: VehicleType) -> List[Vehicle]:
        """
        Retrieve available vehicles of a specific type.
        
        This method queries the inventory management system to get vehicles
        that match the specified type (e.g., CAR, BIKE).
        
        Args:
            vehicleType (VehicleType): The type of vehicle to retrieve
            
        Returns:
            List[Vehicle]: List of available vehicles of the specified type
            
        Note:
            Currently returns all vehicles regardless of type. In a production
            system, this would filter by the specified vehicle type.
        """
        return self.inventoryManagement.get_vehicles()


    #addVehicles, update vehicles, use inventory management to update those.


    def set_vehicles(self, vehicles: List[Vehicle]) -> None:
        """
        Initialize the store's vehicle inventory.
        
        This method sets up the inventory management system with the provided
        list of vehicles.
        
        Args:
            vehicles (List[Vehicle]): List of vehicles to add to this store's inventory
        """
        self.inventoryManagement = VehicleInventoryManagement(vehicles)


    def create_reservation(self, vehicle: Vehicle, user: User) -> Reservation:
        """
        Create a new reservation for a vehicle and user.
        
        This method creates a new reservation object, adds it to the store's
        reservation list, and returns the reservation for further processing.
        
        Args:
            vehicle (Vehicle): The vehicle being reserved
            user (User): The user making the reservation
            
        Returns:
            Reservation: The newly created reservation object
        """
        reservation = Reservation()
        reservation.create_reserve(user,vehicle)
        self.reservations.append(reservation)
        return reservation


    def complete_reservation(self, reservationID: int) -> bool:
        """
        Complete and close a reservation.
        
        This method handles the completion of a rental reservation, including
        removing it from the active reservations list and performing any
        necessary cleanup operations.
        
        Args:
            reservationID (int): The ID of the reservation to complete
            
        Returns:
            bool: True if the reservation was successfully completed
            
        Note:
            This is a placeholder implementation. In production, this would
            include proper reservation lookup, vehicle return processing,
            and status updates.
        """
        #take out the reservation from the list and call complete the reservation method.
        return True

    #update reservation
