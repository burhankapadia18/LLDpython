"""
Extra Cheese Topping Module
==========================

This module implements a concrete Extra Cheese topping class.
It serves as a Concrete Decorator in the Decorator pattern.
"""

from toppings.base_topping import BaseTopping
from pizza.base_pizza import BasePizza


class ExtraCheese(BaseTopping):
    """
    Concrete implementation of the Extra Cheese topping.
    
    This class decorates a pizza by adding extra cheese, increasing
    its price and modifying its name.
    
    Attributes:
        pizza (BasePizza): The pizza being decorated
        price (int): The additional price for extra cheese (10)
    """
    def __init__(self, pizza: BasePizza):
        """
        Initialize a new Extra Cheese topping wrapping around a pizza.
        
        Args:
            pizza (BasePizza): The pizza to decorate with extra cheese
        """
        self.pizza = pizza
        self.price = 10

    def get_price(self):
        """
        Returns the combined price of the pizza and the extra cheese.
        
        Returns:
            int: The total price (base pizza price + 10)
        """
        return self.pizza.get_price() + self.price
    
    def get_name(self):
        """
        Returns the name of the pizza with extra cheese.
        
        Returns:
            str: The modified name of the pizza with " with extra cheese" appended
        """
        return self.pizza.get_name() + " with extra cheese"
