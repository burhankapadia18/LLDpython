"""
Car Rental System - Main Entry Point

This module serves as the main entry point for the car rental system demonstration.
It initializes sample data (users, vehicles, stores) and demonstrates the complete
rental workflow including user search, vehicle reservation, billing, and payment.

The main workflow includes:
1. User searches for stores based on location
2. User browses available vehicles
3. User makes a reservation
4. System generates a bill
5. User makes payment
6. User completes the trip and returns the vehicle
"""

from user import User
from product.car import Car
from store import Store
from vehicle_rental_system import VehicleRentalSystem
from location import Location
from bill import Bill
from payment import Payment
from product.vehicle import VehicleType


def addVehicles():
    """
    Create and initialize sample vehicles for the rental system.
    
    Returns:
        List[Vehicle]: A list of sample vehicles (cars) with assigned IDs
    """
    vehicles = []
    vehicle1 = Car()
    vehicle1.set_vehicle_id(1)
    vehicle2 = Car()
    vehicle2.set_vehicle_id(2)
    vehicles.append(vehicle1)
    vehicles.append(vehicle2)
    return vehicles

def addUsers():
    """
    Create and initialize sample users for the rental system.
    
    Returns:
        List[User]: A list of sample users with assigned IDs
    """
    users = []
    user1 = User()
    user1.set_user_id(1)
    users.append(user1)
    return users

def addStores(vehicles):
    """
    Create and initialize sample stores with the provided vehicles.
    
    Args:
        vehicles (List[Vehicle]): List of vehicles to assign to the stores
        
    Returns:
        List[Store]: A list of sample stores with vehicles assigned
    """
    stores = []
    store1 = Store()
    store1.set_store_id(1)
    store1.set_vehicles(vehicles)
    stores.append(store1)
    return stores



def main():
    """
    Main function that demonstrates the complete car rental workflow.
    
    This function orchestrates the entire rental process by:
    1. Setting up sample data (users, vehicles, stores)
    2. Simulating user interactions and rental operations
    3. Demonstrating the complete lifecycle of a rental transaction
    
    The function runs two complete rental scenarios to show the system's capabilities.
    """

    users = addUsers()
    vehicles = addVehicles()
    stores = addStores(vehicles)

    rentalSystem = VehicleRentalSystem(stores, users)

    #0. User comes
    user = users[0]

    #1. user search store based on location
    location = Location(403012, "Bangalore", "Karnataka", "India")
    store = rentalSystem.get_store(location)

    #2. get All vehicles you are interested in (based upon different filters)
    storeVehicles = store.get_vehicles(VehicleType.CAR)

    #3.reserving the particular vehicle
    reservation = store.create_reservation(storeVehicles[0], user)

    #4. generate the bill
    bill = Bill(reservation)

    #5. make payment
    payment = Payment(bill)
    payment.pay_bill()

    #6. trip completed, submit the vehicle and close the reservation
    store.complete_reservation(reservation.reservationId)


    #0. User comes
    user = users[0]

    #1. user search store based on location
    location = Location(403012, "Bangalore", "Karnataka", "India");
    store = rentalSystem.get_store(location);

    #2. get All vehicles you are interested in (based upon different filters)
    storeVehicles = store.get_vehicles(VehicleType.CAR);


    #3.reserving the particular vehicle
    reservation = store.create_reservation(storeVehicles[0], users[0]);

    #4. generate the bill
    bill = Bill(reservation);

    #5. make payment
    payment = Payment(bill)
    payment.pay_bill()

    #6. trip completed, submit the vehicle and close the reservation
    store.complete_reservation(reservation.reservationId)


if __name__ == "__main__":
    main()
