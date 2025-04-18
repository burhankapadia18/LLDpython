"""
Base Topping Module
==================

This module defines the abstract base class for all pizza toppings.
It acts as the Decorator in the Decorator pattern, providing a common interface
for all concrete toppings that will wrap around pizza objects.
"""

from pizza.base_pizza import BasePizza
from abc import ABC, abstractmethod


class BaseTopping(ABC):
    """
    Abstract base class for all pizza toppings.
    
    This class defines the common interface that all concrete topping classes must implement.
    It serves as the Decorator in the Decorator pattern, wrapping around a pizza object
    and extending its functionality.
    
    Attributes:
        pizza (BasePizza): The pizza being decorated
        price (int): The additional price of the topping
    """
    pizza: BasePizza
    price: int
    
    @abstractmethod
    def get_price(self):
        """
        Returns the combined price of the pizza and the topping.
        
        This should be implemented by concrete classes to add the topping price
        to the wrapped pizza's price.
        
        Returns:
            int: The total price
        """
        pass

    @abstractmethod
    def get_name(self):
        """
        Returns the name of the pizza with the topping description.
        
        This should be implemented by concrete classes to modify the wrapped
        pizza's name to include the topping.
        
        Returns:
            str: The modified name
        """
        pass
  