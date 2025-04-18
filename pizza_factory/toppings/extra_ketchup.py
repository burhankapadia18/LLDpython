"""
Extra Ketchup Topping Module
===========================

This module implements a concrete Extra Ketchup topping class.
It serves as a Concrete Decorator in the Decorator pattern.
"""

from toppings.base_topping import BaseTopping
from pizza.base_pizza import BasePizza


class ExtraKetchup(BaseTopping):
    """
    Concrete implementation of the Extra Ketchup topping.
    
    This class decorates a pizza by adding extra ketchup, increasing
    its price and modifying its name.
    
    Attributes:
        pizza (BasePizza): The pizza being decorated
        price (int): The additional price for extra ketchup (5)
    """
    def __init__(self, pizza: BasePizza):
        """
        Initialize a new Extra Ketchup topping wrapping around a pizza.
        
        Args:
            pizza (BasePizza): The pizza to decorate with extra ketchup
        """
        self.pizza = pizza
        self.price = 5

    def get_price(self):
        """
        Returns the combined price of the pizza and the extra ketchup.
        
        Returns:
            int: The total price (base pizza price + 5)
        """
        return self.pizza.get_price() + self.price
    
    def get_name(self):
        """
        Returns the name of the pizza with extra ketchup.
        
        Returns:
            str: The modified name of the pizza with " with extra ketchup" appended
        """
        return self.pizza.get_name() + " with extra ketchup"
