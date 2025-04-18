"""
Margeritta Pizza Module
======================

This module implements a concrete Margeritta pizza class.
It serves as a Concrete Component in the Decorator pattern.
"""

from .base_pizza import BasePizza


class Margeritta(BasePizza):
    """
    Concrete implementation of a Margeritta pizza.
    
    This class represents a basic Margeritta pizza with a fixed price.
    It implements the BasePizza interface and serves as a concrete component
    that can be decorated with various toppings.
    
    Attributes:
        name (str): The name of the pizza ("Margeritta")
        price (int): The base price of the pizza (100)
    """
    def __init__(self):
        """
        Initialize a new Margeritta pizza with default name and price.
        """
        self.name = "Margeritta"
        self.price = 100
        
    def get_price(self):
        """
        Returns the price of the Margeritta pizza.
        
        Returns:
            int: The price of the pizza (100)
        """
        return self.price
    
    def get_name(self):
        """
        Returns the name of the Margeritta pizza.
        
        Returns:
            str: The name of the pizza ("Margeritta")
        """
        return self.name
