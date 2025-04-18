"""
Pizza Factory Main Module
========================

This module serves as the entry point for the Pizza Factory application.
It demonstrates how to use the Decorator pattern to compose pizzas with different toppings.
"""

from pizza.margeritta import Margeritta
from toppings.extra_cheese import ExtraCheese
from toppings.extra_ketchup import ExtraKetchup


def main():
    """
    Main function demonstrating the usage of the Pizza Factory.
    
    Creates a Margeritta pizza with extra cheese and extra ketchup toppings,
    and displays its name and total price.
    """
    pizza = ExtraKetchup(ExtraCheese(Margeritta()))
    print(f"Price of {pizza.get_name()} is {pizza.get_price()}")


if __name__ == "__main__":
    main()
