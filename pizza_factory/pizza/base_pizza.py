"""
Base Pizza Module
================

This module defines the abstract base class for all pizza types.
It establishes the required interface that all concrete pizzas must implement.
"""

from abc import ABC, abstractmethod

class BasePizza(ABC):
    """
    Abstract base class for all pizzas.
    
    This class defines the common interface that all concrete pizza classes must implement.
    Acts as the Component in the Decorator pattern.
    
    Attributes:
        name (str): The name of the pizza
        price (int): The base price of the pizza
    """
    name: str
    price: int

    @abstractmethod
    def get_price(self):
        """
        Returns the price of the pizza.
        
        Returns:
            int: The price of the pizza
        """
        pass

    @abstractmethod
    def get_name(self):
        """
        Returns the name of the pizza.
        
        Returns:
            str: The name of the pizza
        """
        pass
